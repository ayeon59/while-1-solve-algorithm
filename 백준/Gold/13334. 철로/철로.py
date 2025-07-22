import heapq
import sys
input = sys.stdin.readline

n = int(input())
people = []

for _ in range(n):
    a, b = map(int, input().split())
    start, end = min(a, b), max(a, b)
    people.append((start, end))

trail = int(input())

people.sort(key=lambda x: x[1])

heap = []
max_count = 0

for start, end in people:
    if end - start > trail:
        continue
    heapq.heappush(heap, start)
    while heap and heap[0] < end - trail:
        heapq.heappop(heap)

    max_count = max(max_count, len(heap))

print(max_count)