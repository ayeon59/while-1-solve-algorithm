from sys import setrecursionlimit
setrecursionlimit(10**5)

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if island[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    island = [list(map(int, input().split())) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    count = 0

    for i in range(m):
        for j in range(n):
            if island[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    print(count)
