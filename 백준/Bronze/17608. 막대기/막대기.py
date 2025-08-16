import sys
input = sys.stdin.readline

stack = []
n = int(input())

for _ in range(n):
    stack.append(int(input()))

cnt = 1 
max_height = stack[-1]  

for i in range(n-2, -1, -1):
    if stack[i] > max_height:
        cnt += 1
        max_height = stack[i]

print(cnt)
