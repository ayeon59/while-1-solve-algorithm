from collections import deque

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

def melt():
    temp = [[ice[i][j] for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0:
                water = 0
                for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0:
                        water += 1
                temp[i][j] = max(0, ice[i][j] - water)
    return temp

def count_island():
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                q = deque()
                q.append((i, j))
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if ice[nx][ny] != 0 and not visited[nx][ny]:
                                visited[nx][ny] = 1
                                q.append((nx, ny))
    return cnt

year = 0
while True:
    cnt = count_island()
    if cnt == 0:
        print(0)
        break
    if cnt >= 2:
        print(year)
        break
    ice = melt()
    year += 1
