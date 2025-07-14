n = int(input())
count = 0

col_used = [False] * n
diag_left = [False] * (2 * n)  
diag_right = [False] * (2 * n)

def dfs(row):
    global count
    if row == n:
        count += 1
        return
    for col in range(n):
        if col_used[col] or diag_left[row + col] or diag_right[row - col + n]:
            continue
        col_used[col] = diag_left[row + col] = diag_right[row - col + n] = True
        dfs(row + 1)
        col_used[col] = diag_left[row + col] = diag_right[row - col + n] = False

dfs(0)
print(count)
