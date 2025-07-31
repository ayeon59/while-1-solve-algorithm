import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    member = []
    for _ in range(n):
        a, b = map(int, input().split())
        member.append((a, b))

    member.sort()

    cnt = 1  
    best_interview = member[0][1]  

    for i in range(1, n):
        if member[i][1] < best_interview:
            cnt += 1
            best_interview = member[i][1]

    print(cnt)
