n, s = map(int,input().split())
number = list(map(int,input().split()))
count = 0

def dfs(step,sum):
    global count
    if step == n :
        if sum == s:
            count+= 1
        return 
    dfs(step+1,sum + number[step])
    dfs(step+1,sum)

dfs(0,0)
if s == 0:
    count -= 1
print(count)
