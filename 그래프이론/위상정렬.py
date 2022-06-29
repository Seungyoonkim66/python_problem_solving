from collections import deque


v,e = map(int, input().split())
indegree = [0] * (v+1) # 모든 노드에 대한 진입차수 정보를 표시하는 테이블 (0으로 초기화)
graph = [[] for _ in range(v+1)] # 각 노드에 연결된 간선 정보를 받기 위한 연결 리스트 (그래프)

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b) # a -> b 간선을 표시 
    indegree[b] += 1 # 노드b의 진입차수 + 1

def topology_sort():
    result = []
    q = deque()

    # 모든 노드를 확인 > 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]: # 현재 노드에 연결된 노드 모두 확인
            indegree[i] -= 1 # 현재 노드와 인접 노드 연결된 간선 지우기 -> 인접 노드의 진입차수 -1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()