n, m= map(int,input().split())
ans = []
number=list(map(int,input().split()))

number.sort()

def dfs(cnt,lst,start):
    if cnt == m :
        ans.append(lst)
        return
    for i in range(start,n):
        dfs(cnt+1,lst+[number[i]],i)
        

dfs(0,[],0)

for x in ans :
    print(*x)
    

