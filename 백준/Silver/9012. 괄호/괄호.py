import sys
input = sys.stdin.readline
isDone = False
stack = []

n = int(input())
for _ in range(n):
    isDone = False
    stack = []
    a=input().rstrip()
    for x in a:
        if x =='(' :
            stack.append(x)
        else :
            if not stack : 
                isDone = True
                print("NO")
                break
            stack.pop()
        
    if not isDone:
        if not stack : 
            print("YES")
        else :
            print("NO")

