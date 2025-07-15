import math

m = int(input())
n = int(input())

min = 10**9
sum = 0

left = math.ceil((m)**0.5)
right = math.ceil((n)**0.5)
for i in range(left-1,right+1):
    if m <= i ** 2 <= n: 
        if i**2 < min :
            min = i**2
        sum += i**2
if not sum :
    print(-1)
else :      
    print(sum)
    print(min)