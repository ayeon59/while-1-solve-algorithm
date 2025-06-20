n, m =map(int,input().split())
set_list=set()
result = []
number = list(map(int,input().split()))
number.sort()
ans = []
def dfs(step,lst):
    if step == m:
        ans.append(lst)
        return
    
    for j in range(n):
        dfs(step+1,lst+[number[j]])
        
dfs(0,[])

for element in ans:
    t = tuple(element)
    if t not in set_list:
        set_list.add(t)
        result.append(element)
for x in result:
    print(*x)