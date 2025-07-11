
n = int(input())
sum = 0
if n < 100:
    print(n)
else :  
    for i in range(100,n+1): 
        shouldBreak = False
        num = str(i)
        for j in range(len(num)-2) :
            if int(num[j])-int(num[j+1])!=int(num[j+1])-int(num[j+2]):
                shouldBreak = True
        if shouldBreak : continue
        sum += 1

    print(sum+99)        
