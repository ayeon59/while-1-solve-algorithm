n = int(input())
cnt = 0
for _ in range(n):
    word = list(input())
    num = len(set(word))-1
    check = 0
    for i in range(len(word)-1):
        if(word[i]!=word[i+1]):
            check += 1
    if(check == num):
        cnt += 1
print(cnt)
