INF = int(1e9)

n = int(input()) # 노드의 개수 입력받기
m = int(input()) # 간선의 개수 입력받기
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 경로는 0 으로 초기화 
for a in range(1, n+1): 
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력 받아 초기화 
for _ in range(m):
    a, b, c = map(int, input().split()) 
    graph[a][b] = c # a에서 b로 가는 비용이 c

# graph = [
#     [1000000000, 1000000000, 1000000000, 1000000000, 1000000000], # 사실상 여기는 무시하는 부분 
#     [1000000000, 0, 4, 1000000000, 6], # 각 라인의 0번째 부분도 무시 
#     [1000000000, 3, 0, 7, 1000000000], 
#     [1000000000, 5, 1000000000, 0, 4], 
#     [1000000000, 1000000000, 1000000000, 2, 0]
# ]

# 점화식 수행 
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
