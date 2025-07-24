import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()
bomb_len = len(bomb)

stack = []

for ch in string:
    stack.append(ch)
    if len(stack) >= bomb_len:
        if ''.join(stack[-bomb_len:]) == bomb:
            for _ in range(bomb_len):
                stack.pop()


result = ''.join(stack)
print(result if result else "FRULA")
