n = int(input())
num_list = list(map(int, input().split()))
calculate = list(map(int, input().split()))  

max_val = -int(1e9)
min_val = int(1e9)

def dfs(step, current):
    global max_val, min_val

    if step == n:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return

    for i in range(4):
        if calculate[i] > 0:
            calculate[i] -= 1

            if i == 0:  # +
                dfs(step + 1, current + num_list[step])
            elif i == 1:  # -
                dfs(step + 1, current - num_list[step])
            elif i == 2:  # *
                dfs(step + 1, current * num_list[step])
            else:  # //
                if current < 0:
                    dfs(step + 1, -(-current // num_list[step]))
                else:
                    dfs(step + 1, current // num_list[step])

            calculate[i] += 1  # 백트래킹 

dfs(1, num_list[0])  # 첫 숫자부터 시작 (step=1)
print(max_val)
print(min_val)
