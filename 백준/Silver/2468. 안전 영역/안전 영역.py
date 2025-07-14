import sys
sys.setrecursionlimit(200_000)

n = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_h = max(max(row) for row in graph)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y, h):
   
    visited[x][y] = True
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > h and not visited[nx][ny]:
                dfs(nx, ny, h)

answer = 0
for h in range(max_h):                  
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                dfs(i, j, h)
                cnt += 1             
    answer = max(answer, cnt)

print(max(answer, 1))                  
