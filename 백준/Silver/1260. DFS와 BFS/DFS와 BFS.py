from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()


def dfs(node, visited):
    visited[node] = True
    print(node, end=' ')
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    print(start, end=' ')
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                print(neighbor, end=' ')
                queue.append(neighbor)


visited = [False] * (n + 1)
dfs(v, visited)
print()

visited = [False] * (n + 1)
bfs(v)
