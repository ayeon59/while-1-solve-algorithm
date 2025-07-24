import sys
from collections import deque
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    n, m = map(int, input().split())
    doxc_list = list(map(int, input().split()))
    
    queue = deque([(i, p) for i, p in enumerate(doxc_list)])
    count = 0

    while queue:
        cur = queue.popleft()
        if any(cur[1] < doxc[1] for doxc in queue):  
            queue.append(cur)
        else:
            count += 1
            if cur[0] == m:
                print(count)
                break

