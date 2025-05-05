n, m =map(int,input().split())
arr = [[0]*m for _ in range(n)]

for i in range(n):    
    k = 0
    a = list(map(int,input().split()))
    for k in range(m):
        arr[i][k] = a[k]

for i in range(n):    
    k = 0
    a = list(map(int,input().split()))
    for k in range(m):
        arr[i][k] += a[k]


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()