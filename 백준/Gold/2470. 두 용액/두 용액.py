import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

best = float('inf')
L, R = 0, n - 1
ans_l, ans_r = arr[L], arr[R]

if(ans_l>=0):
    print(arr[0], arr[1])
    sys.exit()

if(ans_r<=0):
    print(arr[-2], arr[-1])
    sys.exit()

while L < R:
    s = arr[L] + arr[R]
    if abs(s) < abs(best):
        best = s
        ans_l, ans_r = arr[L], arr[R]
        if s == 0:     
            break
    if s > 0:
        R -= 1
    else:           
        L += 1

print(ans_l, ans_r)
