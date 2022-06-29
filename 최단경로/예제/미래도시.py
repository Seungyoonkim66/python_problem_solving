import sys

INF = int(1e9)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x, k = map(int, input().split())

# n = 5
# m = 7
# graph = [
#     [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000], 
#     [1000000000, 0, 1, 1, 1, 1000000000], 
#     [1000000000, 1, 0, 1000000000, 1, 1000000000], 
#     [1000000000, 1, 1000000000, 0, 1, 1], 
#     [1000000000, 1, 1, 1, 0, 1], 
#     [1000000000, 1000000000, 1000000000, 1, 1, 0]
# ]
# x = 4
# k = 5

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance == INF:
    print(-1)
else :
    print(distance)