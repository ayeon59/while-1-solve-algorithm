n = int(input())
comparison = list(input().split())
digits = [i for i in range(10)]
visited = [False] * 10
answer_list = []

def dfs(num, depth):
    if depth == n:
        answer_list.append(''.join(map(str, answer)))
        return
    for i in range(10):
        if not visited[i]:
            if comparison[depth] == "<":
                if num < digits[i]:
                    visited[i] = True
                    answer.append(digits[i])
                    dfs(digits[i], depth + 1)
                    answer.pop()
                    visited[i] = False
            else:
                if num > digits[i]:
                    visited[i] = True
                    answer.append(digits[i])
                    dfs(digits[i], depth + 1)
                    answer.pop()
                    visited[i] = False

for i in range(10):
    visited[i] = True
    answer = [digits[i]]
    dfs(digits[i], 0)
    visited[i] = False


answer_list.sort()
print(answer_list[-1])
print(answer_list[0])
