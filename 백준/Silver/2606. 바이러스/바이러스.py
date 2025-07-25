computer = int(input())
network = int(input())
visited = [False] * (computer+1)
virus = [[] for _ in range(computer+1)]


def dfs(v_computer):
    visited[v_computer] = True
    for next_computer in virus[v_computer]:
        if not visited[next_computer]:            
            dfs(next_computer)

for i in range(network):
    a,b = map(int,input().split())
    virus[a].append(b)
    virus[b].append(a)


dfs(1)
print(visited.count(True)-1)
