t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    total = int(input())

    dp = [0] * (total + 1)
    dp[0] = 1  # 0원을 만드는 방법은 '아무 동전도 안 쓰는 것' 1가지

    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] += dp[j - coin]

    print(dp[total])
