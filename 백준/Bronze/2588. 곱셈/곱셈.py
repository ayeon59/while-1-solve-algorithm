a = int(input())
b = int(input())
sum = 0
for i in range(3):
    print(a*(b%10))
    sum += (a*(b%10))*10**i
    b = b//10
    
print(sum)

