n, k = map(int,input().split())
weights=[0]
values=[0]
dp = [[0] * (k+1) for _ in range(n+1)]
for _ in range(n):
    a,b = map(int,input().split())
    weights.append(a)
    values.append(b)

for stuff in range(1,n+1):
    #배낭의무게
    for j in range(k+1):
        if weights[stuff] > j :
            dp[stuff][j] = dp[stuff-1][j]
        else :
            dp[stuff][j] = max(dp[stuff-1][j],dp[stuff-1][j-weights[stuff]]+values[stuff])


print(dp[n][k])