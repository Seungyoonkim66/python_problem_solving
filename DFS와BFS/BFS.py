def search(graph, start):
    need_visited = [start]
    visited = []

    while need_visited:
        node = need_visited.pop()
        # node = need_visited[0]
        # del need_visited[0]

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited


