n, r, c = map(int, input().split())
count = 0
x, y = 0, 0

while n > 0:
    size = 2 ** (n - 1)
    square = size * size

    
    if r < x + size and c < y + size:
        pass  # count += 0

    
    elif r < x + size and c >= y + size:
        count += square
        y += size

    
    elif r >= x + size and c < y + size:
        count += square * 2
        x += size


    else:
        count += square * 3
        x += size
        y += size

    n -= 1

print(count)
