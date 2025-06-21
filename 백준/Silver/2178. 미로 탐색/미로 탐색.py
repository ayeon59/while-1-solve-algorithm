from collections import deque

n, m = map(int,input().split())
miro = []
ans = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    miro.append(list(map(int, input())))

def bfs(x,y):
    q = deque()
    q. append((x,y))

    while q :
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i] 
            ny = cy + dy[i]

            if 0<=nx<n and 0<=ny<m and miro[nx][ny]==1:
                q.append((nx,ny))
                miro[nx][ny] += miro[cx][cy]
                




bfs(0,0)

print(miro[n-1][m-1])