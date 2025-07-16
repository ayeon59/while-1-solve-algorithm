n = int(input())
count = 0
current = 666

while True:
    if "666" in str(current):
        count += 1
        if count == n:
            print(current)
            break
    current += 1
