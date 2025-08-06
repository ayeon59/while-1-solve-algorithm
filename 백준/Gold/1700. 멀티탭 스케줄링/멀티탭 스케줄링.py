n, k = map(int,input().split())
arr = list(map(int,input().split()))
power = []
start = 0
cnt = 0
for i in range(k):
    if len(power) == n :
        start = i
        break 
    if arr[i] in power :
        continue
    else :
        power.append(arr[i])

arr = arr[start:k]
i = 0
while arr :
    if arr[i] in power :
        arr.remove(arr[i])
        continue
    # 플러그 교체 해야 하는 상황
    else :
        max_index = 0
        null_index = 0
        # 교체해야 할 플러그 결정
        for j in range(len(power)) :
            # 이후에 사용할 횟수 남아있는 기기중에 더 먼 기기
            if power[j] in arr:
                max_index = max(max_index,arr.index(power[j]))
            else:
                null_index = power[j]
                break
        if null_index == 0:
            power.remove(arr[max_index])
        else : 
            power.remove(null_index)
        power.append(arr[i])
        arr.remove(arr[i])
        cnt += 1
        
print(cnt)