import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())


board = [[0]*(M+1) for _ in range(N+1)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1

visited = [[False]*(M+1) for _ in range(N+1)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    size = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 1 <= nx <= N and 1 <= ny <= M:
                if board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    size += 1
                    q.append((nx, ny))
    return size

max_size = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j] and not visited[i][j]:
            max_size = max(max_size, bfs(i, j))

print(max_size)
