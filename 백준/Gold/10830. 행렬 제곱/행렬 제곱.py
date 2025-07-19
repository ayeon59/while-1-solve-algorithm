import sys
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def mul(A, B):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def power(matrix, exp):
    if exp == 1:
        return [[element % 1000 for element in row] for row in matrix]
    
    half = power(matrix, exp // 2)
    if exp % 2 == 0:
        return mul(half, half)
    else:
        return mul(mul(half, half), matrix)

result = power(matrix, b)

for row in result:
    print(*row)
