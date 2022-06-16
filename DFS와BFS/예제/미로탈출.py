n = 5
m = 6
graph = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))

def bfs(x,y):
    print(graph[x][y])
    

cnt = 1
for i in range(n):
    for j in range(m):
        bfs(i,j)

