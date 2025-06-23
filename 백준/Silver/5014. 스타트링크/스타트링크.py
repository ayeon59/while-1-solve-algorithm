from collections import deque

f, s, g, u, d = map(int, input().split())
v = [0] * (f + 1)  # f는 1부터 시작해서 f까지면 f+1개만 있으면 충분함

def bfs(start):
    q = deque()
    q.append(start)
    v[start] = 1

    while q:
        c = q.popleft()
        for next in (c + u, c - d):
            if 1 <= next <= f and v[next] == 0:
                v[next] = v[c] + 1
                q.append(next)

if s == g:
    print(0)
else:
    bfs(s)
    if v[g] == 0:
        print("use the stairs")
    else:
        print(v[g] - 1)
