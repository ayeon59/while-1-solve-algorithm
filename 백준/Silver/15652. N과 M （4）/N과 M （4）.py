n, s = map(int,input().split())
ans = []

def dfs(step,num,lst):
    if step == s :
        ans.append(lst)
        return
    for j in range(num,n+1):
        dfs(step+1,j,lst+[j])

dfs(0,1,[])

for x in ans :
    print(*x)
    
