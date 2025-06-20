n, m =map(int,input().split())


number = list(map(int,input().split()))
set_list=set(number)
number_new = sorted(list(set_list))

ans = []
def dfs(step,start,lst):
    if step == m:
        ans.append(lst)
        return
    for i in range(start,len(number_new)):
        dfs(step+1,i,lst+[number_new[i]])        
dfs(0,0,[])

for x in ans:
    print(*x)

