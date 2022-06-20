from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# n = 4
# m = 6
# maze = [
#     [1,0,1,1,1,1], 
#     [1,0,1,0,1,0], 
#     [1,0,1,0,1,1], 
#     [1,1,1,0,1,1]
# ]
q = deque([(0,0)])
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx,ny))

print(maze[n-1][m-1])