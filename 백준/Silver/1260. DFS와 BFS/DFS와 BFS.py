from collections import deque

n,m,v=map(int,input().split())
algorithm = [[False] * (n+1) for _ in range(n+1)]

visited = [False] * (n+1)

for i in range(m):
    a,b = map(int,input().split())
    algorithm[a][b] = True
    algorithm[b][a] = True

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=" ")
    for next in range(n+1) :
        if not visited[next] and algorithm[idx][next] == True:
            dfs(next)

def bfs():
    global q, visited
    while q :
        cur = q.popleft()
        print(cur, end=" ")
        for next in range(n+1):
            if not visited[next] and algorithm[cur][next] == True:
                visited[next] = True
                q.append(next)


dfs(v)
print() 
visited = [False] * (n+1)
q = deque([v])
visited[v] = True
bfs()


