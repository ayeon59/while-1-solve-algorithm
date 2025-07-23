import sys
input = sys.stdin.readline

n = int(input())
card_sang = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))

card_sang.sort()

# target의 첫 등장 위치 (lower bound)
def lower_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start

# target보다 큰 첫 위치 (upper bound)
def upper_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start

# 개수 구하기: upper - lower
for x in card:
    low = lower_bound(card_sang, x)
    high = upper_bound(card_sang, x)
    print(high - low, end=' ')
