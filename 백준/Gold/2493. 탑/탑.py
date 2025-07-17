import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

stack = []
answer = []

for i in range(n):
    current_height = heights[i]
    #더 높은게 나와서 쓸모 없어진 기준 없애버리기 
    while stack and stack[-1][1] < current_height:
        stack.pop()
    #스택에 뭐가 있으면 == 즉, 나보다 높은게 있으면 그거 출력
    if stack:
        answer.append(stack[-1][0])
    # 내가 도달할 수 있는거 없음
    else:
        answer.append(0)
    # 일단 넣고 더 놓은거 나오면 알아서 빠질거임
    stack.append((i + 1, current_height))

print(*answer)
