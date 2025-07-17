t = int(input())
a = [1, 2, 3]

def dfs(c_sum):
    global count
    if c_sum == n:
        count += 1
        return
    if c_sum > n:
        return
    for i in a:
        dfs(c_sum + i)

for _ in range(t):
    n = int(input())
    count = 0
    dfs(0)
    print(count)
