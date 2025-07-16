n = int(input())
egg_list = [list(map(int,input().split())) for _ in range(n)]
max_broken = 0

def dfs(current):
    global max_broken
    if current == n:
        broken = sum(1 for egg in egg_list if egg[0] <= 0)
        max_broken = max(max_broken, broken)
        return
    
    if egg_list[current][0] <= 0:
        dfs(current + 1)
        return
    
    is_hit = False
    for i in range(n):
        if i == current or egg_list[i][0] <= 0:
            continue

        is_hit = True

        egg_list[current][0] -= egg_list[i][1]
        egg_list[i][0] -= egg_list[current][1]
        dfs(current + 1)
        egg_list[current][0] += egg_list[i][1]
        egg_list[i][0] += egg_list[current][1]


    
    if not is_hit:
        dfs(current + 1)

dfs(0)
print(max_broken)