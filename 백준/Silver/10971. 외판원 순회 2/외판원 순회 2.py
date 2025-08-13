#외판원 순회2
n = int(input())
cost_city = []
visited = [0] * n
for _ in range(n):
    cost_city.append(list(map(int,input().split())))

def dfs(start,next,visited,cost,depth):
    global min_cost, start_city
    #이미 최소 비용보다 값이 커졌다면 버릴케이스
    if (min_cost < cost): return
    #모든 도시를 돌았을때 갱신여부 확인
    if depth == n-1:
        if cost_city[next][start_city] != 0 :
            if (cost+cost_city[next][start_city]<min_cost):
                min_cost = cost+cost_city[next][start_city]
        return
    
    #다음 방문할 도시 정하기
    
    for i in range(n):
        #방문한 도시가 아니고, 비용이 0 즉, 자기자신이 아니라면 방문
        if visited[i] != 1 and cost_city[next][i] != 0 :
            #다음에 방문할 도시 체크
            visited[i] = 1
            dfs(next,i,visited,cost+cost_city[next][i],depth+1)
            visited[i] = 0
            


min_cost = 10**8
start_city = 0
for i in range(n):
    #새로운 출발지를 설정하면 방문여부배열 초기화 필요
    #이번 경로의 비용을 담을 변수 초기화
    visited = [0] * n
    #출발지 노드는 방문 처리
    visited[i] = 1
    start_city = i
    dfs(i,i,visited,0,0)
    

print(min_cost)