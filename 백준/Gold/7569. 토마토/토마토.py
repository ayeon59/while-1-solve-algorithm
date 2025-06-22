from collections import deque

m, n, h = map(int, input().split())
tomato = []
date = 0
dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

for _ in range(h):
    floor = []
    for _ in range(n):
        row = list(map(int, input().split()))
        floor.append(row)
    tomato.append(floor)

visited = [[[False]*m for _ in range(n)] for _ in range(h)]

def bfs(z,y,x):
    
    q = deque()
    

    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomato[z][y][x] == 1:
                    q.append((z, y, x))
                    visited[z][y][x] = True

    while q:
        cz, cy, cx = q.popleft()
        
        for i in range(6):
            nz = cz + dz[i]
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if not visited[nz][ny][nx] and tomato[nz][ny][nx] == 0:
                    visited[nz][ny][nx] = True
                    tomato[nz][ny][nx] = tomato[cz][cy][cx] + 1
                    q.append((nz, ny, nx))

bfs(0,0,0)


max_day = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato[z][y][x] == 0:
                print(-1)
                exit()
            max_day = max(max_day, tomato[z][y][x])

print(max_day - 1)
