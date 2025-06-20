from itertools import combinations
from collections import deque

student = [list(input()) for _ in range(5)]
ans = 0


positions = [(i, j) for i in range(5) for j in range(5)]

def is_connected(combo):
    q = deque([combo[0]])
    visited = set([combo[0]])
    count = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in combo and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
                count += 1
    return count == 7


for combo in combinations(positions, 7):
    s_count = 0
    for x, y in combo:
        if student[x][y] == 'S':
            s_count += 1
    if s_count >= 4 and is_connected(combo):
        ans += 1

print(ans)
