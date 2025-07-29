from collections import deque
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)


for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))  
    indegree[x] += 1

count = [[0]*(n+1) for _ in range(n+1)]  # count[i][j]: i를 만들기 위해 j가 몇 개 필요한가
queue = deque()


for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)
        count[i][i] = 1

while queue:
    now = queue.popleft()
    for next, num in graph[now]: 
        for i in range(1, n+1):
            count[next][i] += count[now][i] * num
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, n+1):
    if count[n][i] > 0:
        print(i, count[n][i])
