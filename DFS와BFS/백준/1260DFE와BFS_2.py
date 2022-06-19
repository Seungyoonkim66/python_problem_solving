from collections import deque


def dfs(graph, start, visited):
    visited.append(start)
    print(start, end=" ")
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
            
def bfs(graph, start):
    q = deque([start])
    visited = [start]        

    while q:
        node = q.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if i not in visited:
                q.append(i)
                visited.append(i)


n, m, v = map(int, input().split())
graph =[list() for _ in range(n+1)]
for _ in range(m):
    src, dest =  map(int, input().split())
    graph[src].append(dest)
    graph[dest].append(src)
for i in range(len(graph)):
    graph[i].sort()

dfs(graph, v, visited=[])
print()
bfs(graph, v)
