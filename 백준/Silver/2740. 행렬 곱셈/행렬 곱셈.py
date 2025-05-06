n1, m1 = map(int,input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n1)]
n2, m2 = map(int,input().split())
matrix2 = [list(map(int, input().split())) for _ in range(n2)]
matrix3 = [[0]*m2 for _ in range(n1)]

for i in range(n1):
    for j in range(m2):
        for k in range(m1):
            matrix3[i][j] += matrix1[i][k]*matrix2[k][j]

for i in range(n1):
    print(*matrix3[i])