n = int(input())
m = 0
a=[]
for i in range(n):
    m = int(input())
    a.append(m)
        
a.sort()

for num in a:
    print(num)
