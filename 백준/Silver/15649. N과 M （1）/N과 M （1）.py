N,M = map(int,input().split())

ans = []
visited = [0] * (N+1)

def dfs(n,lst):
    if n == M :
        ans.append(lst)
        return
    
    for i in range(1,N+1):
        if visited[i]==0 :
            visited[i] = 1
            dfs(n+1,lst+[i])
            visited[i] = 0


dfs(0,[])
for element in ans:
    print(*element)