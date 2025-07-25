import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

visited = [False] * (v + 1)
min_heap = []
heapq.heappush(min_heap, (0, 1))  
total_weight = 0

while min_heap:
    cost, now = heapq.heappop(min_heap)

    if visited[now]:
        continue
    visited[now] = True
    total_weight += cost

    for next_cost, next_node in graph[now]:
        if not visited[next_node]:
            heapq.heappush(min_heap, (next_cost, next_node))

print(total_weight)
