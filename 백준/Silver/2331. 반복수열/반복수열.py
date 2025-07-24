a, pow_num = map(int,input().split())
list_num = []
visited = [False] * 200
list_num.append(a)

def calculate_num(number) :
    sum = 0
    while number > 0 :
        sum += pow(number%10,pow_num)
        number //= 10
    return sum
        

while True :
    num = list_num[-1] 
    
    next = calculate_num(num)
    if next in list_num :
        break
    list_num.append(next)
count = 0
for x in list_num:
    if x == next :
        break
    count += 1

print(count)

