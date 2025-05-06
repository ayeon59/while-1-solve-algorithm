a, b, count = map(int, input().split())

for _ in range(count):
    a = (a % b) * 10
print(a // b)
