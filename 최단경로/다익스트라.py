import heapq
from math import dist
import sys


input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split()) # 노드와 간선 개수 입력 받기 
start = int(input()) # 시작 노드 입력 받기 
graph = [[] for _ in range(n+1)] # 각 노드에 연결된 노드 정보 입력 받기 
distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화 

# for _ in range(m): # 간선 정보 입력받기 
#     a,b,c = map(int, input().split()) # a노드에서 b노드로 가는 비용이 c
#     graph[a].append((b,c))

graph = [
    [],  
    [(2, 2), (3, 5), (4, 1)], # 1번 노드의 인접 노드 = 2,3,4
    [(3, 3), (4, 2)], # 2번 노드의 인접 노드 = 3, 4 
    [(2, 3), (6, 5)], 
    [(3, 3), (5, 1)], 
    [(3, 1), (6, 2)], 
    []
]

def dijkstra(start: int):
    q = []
    heapq.heappush(q, (0, start)) # 거리가 0 인 start 노드를 힙에 push 
    distance[start] = 0 # 시작 노드는 거리가 0

    while q: # 힙이 빌 때까지 
        
        dist, now = heapq.heappop(q) # 현재 다룰 노드 now의 거리는 dist 
        print("현재 노드 :", now, " 거리 : ", dist)
        print(distance)
        print("최단 거래 테이블 현 상태: ", distance[now])
        
        if distance[now] < dist : # 최단 거리 테이블에 적힌 값이 현재 노드의 거리보다 작다면 
            continue # 그대로 두고 넘어감 

        for i in graph[now]: # 현재 노드의 인접 노드를 하나씩 확인
            print("  인접 노드 :", i)
            cost = dist + i[1] # 비용은 현재 거리와 인접 노드 거리를 더한 값
            print("  인접 노드 비용 : ", cost)
            if cost < distance[i[0]] : # 최단 거리 테이블에 적힌 인접 노드의 경로보다 작은 경우 
                distance[i[0]] = cost # 갱신
                print("  갱신 결과 : ", distance)
                heapq.heappush(q, (cost, i[0])) # 인접 노드 힙에 넣기 

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])