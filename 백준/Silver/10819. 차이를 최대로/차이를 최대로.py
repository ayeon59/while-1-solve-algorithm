from itertools import permutations
n = int(input())
a = list(map(int,input().split()))
sum = 0
max_sum = 0
for p in permutations(a, n):
    sum = 0
    for i in range(n-1):
        sum += abs(p[i]-p[i+1])
    if max_sum < sum :
        max_sum = sum


print(max_sum)