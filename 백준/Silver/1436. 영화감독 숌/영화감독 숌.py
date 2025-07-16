n = int(input())
count_666 = 0
num = str(665)
while count_666 != n :
    num = str(int(num)+1)
    if num.count("666") >= 1 :
        count_666 += 1

print(num)