import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = sorted([int(input()) for _ in range(n)])

def can_set(min_dist):
    count = 1
    last = home[0]
    for i in range(1, n):
        if home[i] - last >= min_dist:
            count += 1
            last = home[i]
    return count >= c


left = 1  
right = home[-1] - home[0]  
answer = 0

while left <= right:
    mid = (left + right) // 2
    if can_set(mid):
        answer = mid 
        left = mid + 1
    else:
        right = mid - 1

print(answer)
