def DFS(L, total, numbers, target):
    global cnt
    if L == len(numbers):
        if total == target:
            cnt += 1
    else:
        DFS(L + 1, total + numbers[L], numbers, target)
        DFS(L + 1, total - numbers[L], numbers, target)

def solution(numbers, target):
    global cnt
    cnt = 0
    DFS(0, 0, numbers, target)
    return cnt
