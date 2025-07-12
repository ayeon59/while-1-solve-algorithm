row, col = map(int,input().split())
cut = int(input())
row_list=[0,row]
col_list=[0,col]
max_row = 0
max_col= 0

for _ in range(cut):
    a,b = map(int,input().split())
    if a == 1 :
        row_list.append(b)
    else :
        col_list.append(b)
row_list.sort()
col_list.sort()

for i in range(len(row_list)-1):
    max_row = max(row_list[i+1]-row_list[i],max_row)    
for i in range(len(col_list)-1):
    max_col = max(col_list[i+1]-col_list[i],max_col) 


print(max_row*max_col)

