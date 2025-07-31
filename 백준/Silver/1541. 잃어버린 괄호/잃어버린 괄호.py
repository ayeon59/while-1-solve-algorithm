expression = input().split('-')

first = sum(map(int, expression[0].split('+')))


rest = 0
for group in expression[1:]:
    rest += sum(map(int, group.split('+')))

print(first - rest)
