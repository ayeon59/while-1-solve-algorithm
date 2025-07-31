import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ground = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

count = 0

def dfs_row(x, y):
    global count
    visited[x][y] = True
    if y == m-1 or ground[x][y+1] == "|":
        count += 1
        return
    if y+1 < m and not visited[x][y+1]:
        dfs_row(x, y+1)

def dfs_col(x, y):
    global count
    visited[x][y] = True
    if x == n-1 or ground[x+1][y] == "-":
        count += 1
        return
    if x+1 < n and not visited[x+1][y]:
        dfs_col(x+1, y)

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if ground[i][j] == '-':
                dfs_row(i, j)
            else:
                dfs_col(i, j)

print(count)