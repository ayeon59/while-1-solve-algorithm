from collections import deque
n = int(input())
m = int(input())
computer = [[] for _ in range(n+1)]
visited = [False] * (n+1) 
count = 0

for _ in range(m):
    a, b = map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)

def bfs(start):
    global count
    q = deque([start])
    visited[start] = True
    while q :
        element = q.popleft()

        for next in computer[element]:
            if not visited[next] :
                count += 1
                visited[next] = True
                q.append(next)

bfs(1)
print(count)