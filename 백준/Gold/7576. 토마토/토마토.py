
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()


for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j, 0))  

max_day = 0


while q:
    x, y, day = q.popleft()
    max_day = max(max_day, day)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = 1  
                q.append((nx, ny, day + 1))


for row in tomato:
    if 0 in row:
        print(-1)
        sys.exit()

print(max_day)
