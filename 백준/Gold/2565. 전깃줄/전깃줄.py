m = int(input())
line = []

# 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    line.append((a, b))

# a기준으로 정렬 (전깃줄이 교차하지 않게 만들기 위해)
line.sort()

# b값만 추출해서 LIS 진행
b_values = [b for a, b in line]

# dp[i]: i번째까지 봤을 때의 LIS 길이
dp = [1] * m

for i in range(1, m):
    for j in range(i):
        if b_values[i] > b_values[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 최장 증가 수열 길이를 전체에서 빼면 -> 제거할 전깃줄 수
print(m - max(dp))
