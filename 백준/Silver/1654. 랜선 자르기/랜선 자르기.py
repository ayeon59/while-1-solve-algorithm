#컴퓨터야 최대 자를 수 있는 길이좀 알려줘라
#너무 긴걸로 자르면 총 갯수를 못뽑고

k,n = map(int,input().split())
line = [int(input()) for _ in range (k)]
length = 0
def how_many_line(cut_length):
    sum = 0
    if cut_length == 0 :
        return
    for x in line :
        sum += x//cut_length
    if sum >= n :
        return True
    else :
        return False

def cut_line(start,end):
    global length
    if start > end :
        return 
    mid = ( start + end ) // 2
    #길이를 더 늘려야 하는 상황
    if how_many_line(mid) :
        length = max(length,mid)
        cut_line(mid+1,end)
    #길이를 더 줄여야 하는 상황
    else :
        cut_line(start,mid-1)

max_length = sum(line) // n
min_num = n//k + 1
min_length = min(line) // min_num + 1

cut_line(min_length,max_length)
print(length)


