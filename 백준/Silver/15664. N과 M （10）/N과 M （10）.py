n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

answer_set = set()

def dfs(start, path):
    if len(path) == m:
        answer_set.add(tuple(path))  # 리스트는 set에 못 들어가니까 튜플로!
        return
    
    for i in range(start, n):
        dfs(i + 1, path + [nums[i]])

dfs(0, [])

for seq in sorted(answer_set):  # 사전순 출력
    print(*seq)
