from collections import deque

a, k = map(int,input().split())


def bfs(me, sister):
    q = deque()
    v = [0] * 200001
    q.append(me)
    v[me] = 1

    while q :
        c = q.popleft()
        if c == sister :
            return v[sister]-1
        for next in (c-1,c+1,c*2):
            if(0<=next<=200000 and v[next]==0):
                q.append(next)
                v[next] = v[c] + 1



ans = bfs(a,k)
print(ans)