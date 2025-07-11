n = int(input())
for _ in range(n):
    a = list(input())
    sum = 0
    acc = 1
    
    for x in a :
        if x == 'O':
            sum += acc
            acc += 1
        else :
            acc = 1
    print(sum)
