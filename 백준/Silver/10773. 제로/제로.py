import sys
input = sys.stdin.readline

stack = []

k = int(input())
for _ in range(k):
    a = int(input())
    if a != 0  :
        stack.append(a)
    else :
        stack.pop()

print(sum(stack))