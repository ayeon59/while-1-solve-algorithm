
n = int(input())
meeting = []
for _ in range(n):
    a, b = map(int,input().split())
    meeting.append([a,b])
meeting.sort(key=lambda x: (x[1], x[0]))
cnt = 0
end_time = 0
for start,end in meeting:
    if start >= end_time :
        cnt += 1
        end_time = end 

print(cnt)
    