n, s = map(int,input().split())
a = list(map(int,input().split()))
count = 0

def dfs(depth,sum):
    global count
    if depth == n :
        if sum == s :
            count += 1
        return
    
    dfs(depth+1,sum + a[depth])
    dfs(depth+1,sum)
            
dfs(0,0)

if s == 0:
    count -=1

print(count)