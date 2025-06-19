n = int(input())
meeting = []

for i in range(n):
    start,end = map(int,input().split())
    meeting.append((start,end))

count = 0
sorted_meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

end_time = 0

for start, end in sorted_meeting:
    if start >= end_time:
        count += 1
        end_time = end

print(count)