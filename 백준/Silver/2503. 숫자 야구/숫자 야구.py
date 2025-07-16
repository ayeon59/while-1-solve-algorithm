n = int(input())
baseball = [list(map(int, input().split())) for _ in range(n)]

candidates = []
for i in range(123, 988):
    num = str(i)
    if '0' in num or len(set(num)) < 3:
        continue
    candidates.append(num)

for q_num, s, b in baseball:
    q_num = str(q_num)
    new_candidates = []
    for c in candidates:
        strike = sum([q_num[i] == c[i] for i in range(3)])
        ball = sum([q_num[i] in c for i in range(3)]) - strike
        if strike == s and ball == b:
            new_candidates.append(c)
    candidates = new_candidates

print(len(candidates))
