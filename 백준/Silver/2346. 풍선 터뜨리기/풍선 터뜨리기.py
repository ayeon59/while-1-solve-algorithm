import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
number = list(map(int,input().split()))
queue = deque()
for i in range(1,n+1):
    queue.append((i,number[i-1]))

result,next = queue.popleft()
print(result, end=" ")
while len(queue)>1 :
    if next > 0 :
        for i in range(next-1):
            result,next = queue.popleft()
            queue.append((result,next))
    else :
        for i in range(abs(next)):
            result,next = queue.pop()
            queue.appendleft((result,next))
        
    result,next = queue.popleft()
    print(result, end=" ")

result,next = queue.popleft()
print(result)