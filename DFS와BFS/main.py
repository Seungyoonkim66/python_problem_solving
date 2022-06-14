import DFS
import BFS

if __name__ == "__main__":
    # graph = dict()
 
    # graph['A'] = ['B', 'C']
    # graph['B'] = ['A', 'D']
    # graph['C'] = ['A', 'G', 'H', 'I']
    # graph['D'] = ['B', 'E', 'F']
    # graph['E'] = ['D']
    # graph['F'] = ['D']
    # graph['G'] = ['C']
    # graph['H'] = ['C']
    # graph['I'] = ['C', 'J']
    # graph['J'] = ['I']

    # print(graph)
    # # print(DFS.search(graph, 'A'))
    # # print(DFS.search_recursive(graph, 'A',[]))
    # print(BFS.search(graph, "A"))

    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]