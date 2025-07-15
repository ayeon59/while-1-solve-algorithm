from itertools import combinations

def find_gcd(a,b):
    max_num = 0
    if a > b :
        a,b = b,a
    for i in range(1,a+1):
        if a%i ==0 and b%i==0 :
            max_num =max(max_num,i) 
    return max_num

n = int(input())
for _ in range(n):
    arr = list(map(int,input().split()))
    max_num = 0
    for a, b in combinations(arr, 2):
        max_num =max(max_num,find_gcd(a,b))
    print(max_num)