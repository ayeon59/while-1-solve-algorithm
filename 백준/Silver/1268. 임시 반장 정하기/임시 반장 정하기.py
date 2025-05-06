student = int(input())
arr = [[0]*5 for _ in range(student)]

cnt = 0
max_cnt = 0
who = 0
for i in range(student):
    friend = list(map(int,input().split()))
    arr[i] = friend


for i in range(student):
    cnt = 0
    for j in range(student):
        if(i==j):
            continue
        for k in range(5):
            if(arr[i][k]==arr[j][k]):
                cnt += 1
                break
    if(max_cnt<cnt):
        max_cnt = cnt
        who = i


print(who+1)