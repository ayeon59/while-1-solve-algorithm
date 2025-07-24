import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
card_sang = list(map(int,input().split()))
m = int(input())
card_list = list(map(int,input().split()))

card_sang.sort()

def check_card(start,end,target):
    if start > end :
        return False
    mid = (start + end) // 2
    if card_sang[mid] == target :
        return True
    elif card_sang[mid] > target :
        return check_card(start,mid-1,target)
    else :
        return check_card(mid+1,end,target)
    return
    

for x in card_list :
    if check_card(0,n-1,x) : print(1 , end=" ")
    else : print(0 , end=" ")


            

        

