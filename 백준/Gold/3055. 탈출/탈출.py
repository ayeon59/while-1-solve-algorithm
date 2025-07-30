import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
road = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    road.append(list(input().strip()))

queue = deque()
start  = ()
finish = ()
# 물이 몇 분 뒤에 차는지 기록할 배열
water_time = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if road[i][j] == '*':
            water_time[i][j] = 0
            queue.append((i,j))
        if road[i][j] == 'S':
            start = (i,j)
        if road[i][j] == 'D':
            finish = (i,j)

# 물 차오르기
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if road[nx][ny] == '.' and water_time[nx][ny] == -1:
                water_time[nx][ny] = water_time[x][y] + 1
                queue.append((nx, ny))

# 고슴도치 이동
visited = [[-1]*m for _ in range(n)]
queue = deque()
queue.append(start)
visited[start[0]][start[1]] = 0
complete_finish = False

while queue:
    x, y = queue.popleft()
    if (x, y) == finish:
        complete_finish = True
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == -1 and (road[nx][ny] == '.' or road[nx][ny] == 'D'):
                next_time = visited[x][y] + 1
                # 물보다 먼저 도착해야 함
                if water_time[nx][ny] == -1 or next_time < water_time[nx][ny]:
                    visited[nx][ny] = next_time
                    queue.append((nx, ny))

if not complete_finish:
    print("KAKTUS")
else:
    print(visited[finish[0]][finish[1]])
