a, b = map(int,input().split())
n = list(map(int,input().split()))

for x in n:
    if x < b :
        print(x,end=" ")