n = int(input())
answer = n
count = 0
while True :
    temp = str(answer%10 + answer//10)
    answer = str(answer)
    answer = answer[-1] + temp[-1]
    count += 1
    answer = int(answer)
    
    if answer == n :
        break

print(count)
            