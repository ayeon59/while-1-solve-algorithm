student = int(input())
arr = [input() for _ in range(student)]
cnt = 1

while True:
    check = [s[-cnt:] for s in arr]
    if len(set(check)) == student:
        break
    cnt += 1

print(cnt)
