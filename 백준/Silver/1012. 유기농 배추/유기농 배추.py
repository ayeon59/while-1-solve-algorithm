import sys
sys.setrecursionlimit(10000)

t = int(input())

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and ground[nx][ny] and not visited[nx][ny]:
            dfs(nx,ny)
    return

for test in range(t):
    m,n,k = map(int,input().split())
    ground = [[False]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    worm = 0
    
    for _ in range(k):
        x, y = map(int,input().split())
        ground[y][x] = True


    for i in range(n):
        for j in range(m):
            if visited[i][j] or not ground[i][j] :
                continue
            dfs(i,j)   
            worm += 1
    print(worm) 

