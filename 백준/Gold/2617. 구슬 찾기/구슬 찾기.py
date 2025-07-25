n, m = map(int,input().split()) 
graph1 = [[0]*(n+1) for _ in range(n+1)]
graph2 = [[0]*(n+1) for _ in range(n+1)]
scope = n//2 + 1

answer = set()

for _ in range(m):
    a,b = map(int,input().split())
    graph1[b][a] = 1
    graph2[a][b] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph1[i][k] == 1 and graph1[k][j] == 1:
                graph1[i][j] = 1
            if graph2[i][k] == 1 and graph2[k][j] == 1:
                graph2[i][j] = 1

for i in range(1,n+1):
    if graph1[i].count(1) >= scope:
        answer.add(i)
    if graph2[i].count(1) >= scope:
        answer.add(i)

print(len(answer))
