import sys
import heapq
input = sys.stdin.readline

v, e = map(int,input().split())
visited = [False] * (v+1)
graph = [[] for _ in range(v+1)]
heap = []
total_weight = 0


def prim(start):
    global total_weight
    visited[start] = True
    for edge in graph[start]:
        heapq.heappush(heap,edge)
        
    while heap :
        weight, next_node= heapq.heappop(heap)
        if not visited[next_node] :
            visited[next_node] = True
            total_weight += weight
            for edge in graph[next_node]:
                if not visited[edge[1]] :
                    heapq.heappush(heap,edge)

for _ in range(e):
    a,b,weight = map(int,input().split())
    graph[a].append((weight,b))
    graph[b].append((weight,a))    

prim(1)
print(total_weight)

