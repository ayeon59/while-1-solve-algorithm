import math

t = int(input())
sum = 1
for _ in range(t):
    n, m = map(int,input().split())
    sum = math.factorial(m)/(math.factorial(n)*math.factorial(m-n))
    print(int(sum))


