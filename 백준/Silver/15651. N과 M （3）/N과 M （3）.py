n, s = map(int,input().split())
ans = []

def dfs(step,lst):
    if step == s:
        ans.append(lst)
        return
    for i in range(1,n+1):
        dfs(step+1,lst+[i])

dfs(0,[])
for x in ans :
    print(*x)
    
