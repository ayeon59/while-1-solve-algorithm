n, m= map(int,input().split())
ans = []
number=list(map(int,input().split()))
visited = [0] * (n)
number.sort()

def dfs(cnt,lst):
    if cnt == m :
        ans.append(lst)
        return
    for i in range(n):
        if visited[i] == 0 :
            visited[i] = 1
            dfs(cnt+1,lst+[number[i]])
            visited[i] = 0
    

dfs(0,[])

for x in ans :
    print(*x)
    

