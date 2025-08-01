n = int(input())

arr=[0,1]
for i in range(2,n+1):
    val = arr[i-1] + arr[i-2]
    arr.append(val)

print(arr[n])