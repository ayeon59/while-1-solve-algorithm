import heapq
import sys
input = sys.stdin.readline

n_city = int(input())
n_bus = int(input())
road = [[] for _ in range(n_city+1)]
cost = [float('inf')] * (n_city + 1)

for _ in range(n_bus):
    a, b, c = map(int,input().split())
    road[a].append((b,c))

start, end = map(int,input().split())

queue = []
heapq.heappush(queue, (0, start)) 
cost[start] = 0

while queue:
    cr_cost, cr_node = heapq.heappop(queue)
    if cost[cr_node] < cr_cost:
        continue
    if cr_node == end:
        print(cr_cost)
        break
    for neighbor, go_cost in road[cr_node]:
        new_cost = cr_cost + go_cost
        if new_cost < cost[neighbor]:
            cost[neighbor] = new_cost
            heapq.heappush(queue, (new_cost, neighbor))
