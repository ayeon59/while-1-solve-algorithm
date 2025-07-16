n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
max_profit = 0
def dfs(day,cost):
    global max_profit
    if day >= n :
        max_profit = max(max_profit,cost)
        return
    dfs(day+1,cost)
    if day+table[day][0] > n : return
    dfs(day+table[day][0],cost+table[day][1])


dfs(0,0)
print(max_profit)