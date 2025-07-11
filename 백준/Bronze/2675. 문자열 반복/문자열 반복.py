n = int(input())
for _ in range(n):
    a, st = input().split()
    a = int(a)
    for x in st :
        for _ in range(a):
            print(x,end="")
    print()            
