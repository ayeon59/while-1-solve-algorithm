import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, target_x, target_y = map(int, input().split())

# 바이러스 정보 (번호, 시간, x, y)
virus_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus_list.append((graph[i][j], 0, i, j))  # (virus_number, time, x, y)

# 번호 낮은 순부터 퍼지므로 정렬
virus_list.sort()

# 큐로 BFS
q = deque(virus_list)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, time, x, y = q.popleft()
    
    if time == s:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
