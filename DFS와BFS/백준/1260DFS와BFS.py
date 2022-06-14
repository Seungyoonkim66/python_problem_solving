from collections import deque


def dfs(graph, start, visited):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def bfs(graph, start):
    q = deque([start])
    visited= [start]

    while q:
        node = q.popleft()
        for i in graph[node]:
            if i not in visited:
                q.append(i)
                visited.append(i)

    return visited



n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()


print(dfs(graph, v, visited=[]))
print(bfs(graph, v))