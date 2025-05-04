def DFS(L):
    if L == m:
        print(*res)
        return
    used = set()  
    for i in range(n):
        if not ch[i] and a[i] not in used:
            used.add(a[i])
            ch[i] = 1
            res[L] = a[i]
            DFS(L + 1)
            ch[i] = 0

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
n = len(a)
res = [0] * m
ch = [0] * n

DFS(0)
