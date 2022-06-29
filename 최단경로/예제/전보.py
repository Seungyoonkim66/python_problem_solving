import heapq
import sys


INF = int(1e9)
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))


# n,m,c = 3,2,1
# distance = [INF] * (n+1)
# graph = [
#     [], 
#     [(2, 4), (3, 2)], 
#     [], 
#     []
# ]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):
            continue
        for adj_node in graph[now]:
            cost = dist + adj_node[1]
            if cost < distance[adj_node[0]]:
                distance[adj_node[0]] = cost
                heapq.heappush(q, (cost, adj_node[0]))

dijkstra(c)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count +=1 
        max_distance = max(max_distance, d)

print(count-1, max_distance)
