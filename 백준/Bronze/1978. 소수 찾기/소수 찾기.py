def is_prime(a):
    if a < 2 :
        return False 
    for i in range(2,int(a**0.5)+1):
        if (a%i==0):
            return False
    return True


n = int(input())
a = list(map(int,input().split()))
num = 0
for x in a:
    if (is_prime(x)) : num += 1
print(num)    