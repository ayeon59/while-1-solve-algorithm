def dfs(step,s,lst):
    if step == 6 :
        result.append(lst)
        return
    for i in range(s,k):
        dfs(step + 1, i + 1, lst + [numbers[i]])


while True:
    ans = list(map(int,input().split()))
    result = []
    k = ans[0]
    if len(ans) == 1 and k == 0 :
        break
    numbers = ans[1:]
    dfs(0,0,[])
    for x in result:
        print(*x)
    print()
    

    