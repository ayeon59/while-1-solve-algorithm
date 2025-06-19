import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
v, e = map(int, input().split())
start = int(input())
distance = [INF] * (v + 1)
place = [[] for _ in range(v + 1)]

for _ in range(e):
    u, node, w = map(int, input().split())
    place[u].append((node, w))

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
        continue
    
    for next, weight in place[now]:
        cost = dist + weight
        if cost < distance[next]:
            distance[next] = cost
            heapq.heappush(q, (cost, next))

for i in range(1, v + 1):
    print("INF" if distance[i] == INF else distance[i])
