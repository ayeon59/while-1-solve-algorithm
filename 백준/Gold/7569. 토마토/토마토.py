from collections import deque

m, n, h = map(int, input().split())
tomato = []
cnt = 0

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
    global cnt
    q = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomato[z][y][x] == 1:
                    q.append((z, y, x))
                    visited[z][y][x] = True

                elif tomato[z][y][x] == 0:
                    cnt += 1

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
                    cnt -= 1
    if cnt == 0 :
        return tomato[cz][cy][cx] - 1
    else :
        return -1


print(bfs(0,0,0))
