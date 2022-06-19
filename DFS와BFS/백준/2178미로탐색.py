# n, m = map(int, input().split())
# maze = [list(input()) for _ in range(n)]


from collections import deque

n = 4
m = 6
maze = [
    ['1', '0', '1', '1', '1', '1'], 
    ['1', '0', '1', '0', '1', '0'], 
    ['1', '0', '1', '0', '1', '1'], 
    ['1', '1', '1', '0', '1', '1']
]
dist = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
q = deque()

q.append((0,0))
visited[0][0] = True 
dist[0][0] = 1

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx,ny))
                dist[nx][ny] = maze[x][y] + 1
                visited[nx][ny] = True
                print(dist)
                


# def bfs(x, y):
#     # 상 하 좌 우 
#     dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

#     # 시작 지점 
#     q = deque([(0,0)])

#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny <= m:
#                 if maze[nx][ny] == 1:
#                     q.append((nx, ny))
#     return maze[n-1][m-1]
# print(bfs(0,0))
#     # if maze[current[0]][current[1]] == 1:
   
#     # print()


