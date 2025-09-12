import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [[0]*(N+1) for _ in range(N+1)]  # 0=빈칸, 1=사과, 2=뱀
K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1

L = int(input())
turns = {}
for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C  # 시간 X가 되었을 때 회전

# 방향: 0=오른쪽, 1=아래, 2=왼쪽, 3=위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0

snake = deque([(1, 1)])   # 머리가 앞(왼쪽)
board[1][1] = 2
time = 0
x, y = 1, 1

while True:
    time += 1
    nx, ny = x + dx[direction], y + dy[direction]

    # 벽 또는 자기 몸에 부딪히면 종료
    if not (1 <= nx <= N and 1 <= ny <= N) or board[nx][ny] == 2:
        print(time)
        break

    if board[nx][ny] == 1:       # 사과 있으면 머리만 늘림
        board[nx][ny] = 2
        snake.appendleft((nx, ny))
    else:                        # 사과 없으면 머리 늘리고 꼬리 줄임
        board[nx][ny] = 2
        snake.appendleft((nx, ny))
        tx, ty = snake.pop()
        board[tx][ty] = 0

    x, y = nx, ny

    # 해당 시각에 방향 전환
    if time in turns:
        if turns[time] == 'L':
            direction = (direction - 1) % 4
        else:  # 'D'
            direction = (direction + 1) % 4
