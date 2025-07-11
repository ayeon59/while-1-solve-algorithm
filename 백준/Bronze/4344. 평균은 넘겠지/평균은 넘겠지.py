c = int(input())

for i in range(c):
    a = list(map(int,input().split()))
    num = a[0] 
    avg_num = 0
    a = a[1:]
    avg = sum(a)/len(a)
    for x in a :
        if x > avg :
            avg_num += 1
    print(f"{((avg_num/len(a))*100):.3f}%")
    