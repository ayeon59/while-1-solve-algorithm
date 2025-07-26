import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while queue :
        cx,cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m :
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[cx][cy] + 1
                    queue.append((nx, ny))


queue = deque([(0,0)])
bfs()
print(maze[n-1][m-1])
