from collections import deque

n = int(input())
apartment=[]
visited = [[0]*n for _ in range(n)]
part = 1
#단지 별 아파트 갯수 저장
ans = []

#아파트 단지 입력받기
for i in range(n):
    apartment.append(list(map(int, input())))

def bfs(x,y):
    q = deque([(x, y)])
    visited[x][y] = 1
    count = 1

    while q :
        cx, cy = q.popleft()
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx = cx + dx
            ny = cy + dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and apartment[nx][ny]==1 :
                q.append((nx,ny))
                visited[nx][ny] = 1
                count += 1
                
    return count

for i in range(n):
    for j in range(n) :
        if apartment[i][j] == 1 and visited[i][j] == 0 :
            ans.append(bfs(i,j))

print(len(ans))
for x in sorted(ans) :
    print(x)
