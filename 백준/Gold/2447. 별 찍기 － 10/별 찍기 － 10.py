n = int(input())

def basic_star_square():

    return ["***",
            "* *",
            "***"]

def zero_star_square():
    
    return ["   ",
            "   ",
            "   "]

def whole_star_square(three):
    if three == 3:
        return basic_star_square()

    sub = whole_star_square(three // 3)
    size = three // 3
    rows = []

    
    for line in sub:
        rows.append(line + line + line)

    for line in sub:
        rows.append(line + (" " * size) + line)


    for line in sub:
        rows.append(line + line + line)

    return rows

for line in whole_star_square(n):
    print(line)
