a = int(input())
b = int(input())
c = int(input())
number = [0]*10
num = str(a*b*c)
for x in num :
    number[int(x)] += 1
for x in number:
    print(x)


