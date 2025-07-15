import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def air_bfs():
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheese[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif cheese[nx][ny] == 1:
                    melt_list.append((nx, ny))
                    visited[nx][ny] = True  

    return

hour = 0
last_cheese_count = 0

while True:
    melt_list = []
    air_bfs()

    if not melt_list:
        break  

    last_cheese_count = len(melt_list)

    for x, y in melt_list:
        cheese[x][y] = 0

    hour += 1

print(hour)
print(last_cheese_count)
