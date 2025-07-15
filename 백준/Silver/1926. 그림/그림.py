from collections import deque
n, m =map(int,input().split())
paint = []
visited = [[False] * (m) for _ in range(n)]
num_paint = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    paint.append(list(map(int,input().split())))




def bfs():
    size = 1
    global q, visited
    while q :
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m :
                if not visited[nx][ny] and paint[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    size += 1
    return size

max_paint = 0
num_paint = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] or not paint[i][j] :
            continue
        q = deque([(i,j)])
        visited[i][j] = True
        max_paint = max(max_paint,bfs())
        num_paint += 1

print(num_paint)
print(max_paint)