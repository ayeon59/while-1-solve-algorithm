import sys
sys.setrecursionlimit(10000)  
input = sys.stdin.readline

n = int(input())
place = input()
take_walk = [[] for _ in range(n+1)]
count = 0

for i in range(n-1):
    a, b = map(int,input().split())
    take_walk[a].append(b)
    take_walk[b].append(a) 

def dfs(next):
    global count
    for neighbor in take_walk[next]:
        if visited[neighbor]:
            continue
        if int(place[neighbor-1]) == 1:
            count += 1
            continue
        visited[next] = True
        dfs(neighbor)

for i in range(1,n+1):
    #실내장소에서 출발
    if int(place[i-1]) == 1:
        visited = [False] * (n+1)
        visited[i] = True
        dfs(i)
print(count)