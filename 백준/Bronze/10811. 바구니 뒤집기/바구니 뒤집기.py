n, m = map(int,input().split())

arr = list(range(1, n + 1))

def reverse_subarray(arr, start, end):
    arr[start:end+1] = arr[start:end+1][::-1]
    return arr

for i in range(m):
    start, end = map(int,input().split())
    reverse_subarray(arr,start-1,end-1)

for x in arr :
    print(x, end=" ")

    