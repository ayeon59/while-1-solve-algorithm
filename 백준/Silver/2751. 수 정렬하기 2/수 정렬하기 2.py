import sys
input = sys.stdin.readline

n = int(input())
numbers = sorted(int(input()) for _ in range(n))
print('\n'.join(map(str, numbers)))
