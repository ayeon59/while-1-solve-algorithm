N, M = map(int, input().split())

def dfs(start, path):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(start, N + 1):
        dfs(i + 1, path + [i])

dfs(1, [])
