n, m = map(int, input().split())
lecture = list(map(int, input().split()))

def check(capacity):
    count = 1
    total = 0
    for lec in lecture:
        if total + lec > capacity:
            count += 1
            total = lec
        else:
            total += lec
    return count <= m

start = max(lecture)
end = sum(lecture)
result = end

while start <= end:
    mid = (start + end) // 2
    if check(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)