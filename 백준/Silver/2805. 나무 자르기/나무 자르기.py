import sys
sys.setrecursionlimit(10**8)

n,m = map(int,input().split())
tree = list(map(int,input().split()))


#특정 길이로 잘랐을 때 몇개의 조각이 나오는지
def cut_part(num):
    sum = 0 
    for x in tree :
        sum += (0 if x - num <= 0 else x-num)
    return sum

max_cut = 0

def find_answer(start,end):
    global max_cut
    if start >= end :
        return
    mid = (start+end)//2
    if cut_part(mid) >= m : 
        max_cut = max(max_cut,mid)
        find_answer(mid+1,end)
    else : 
        find_answer(start,mid)
        

tree.sort()
# quick_sort_tree(tree,0,n-1)
# print(tree)
find_answer(0,tree[-1]+1)
print(max_cut)