def search(graph, start_node):
    need_visitied = [start_node]
    visited = []

    while need_visitied:
        node = need_visitied.pop()

        if node not in visited:
            visited.append(node)
            need_visitied.extend(graph[node])
    
    return visited

def search_recursive(graph, start, visited=[]):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            search_recursive(graph, node, visited)
    return visited 
