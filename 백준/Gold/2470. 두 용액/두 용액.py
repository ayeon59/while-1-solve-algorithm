n = int(input())
solution = list(map(int,input().split()))
solution.sort()
min_sum = float('inf') 
left = 0
right = n-1
min_left = 0
min_right = 0
while(left<right):
    sum = solution[left] + solution[right]
   
    if abs(sum) < abs(min_sum) :
        min_sum=sum
        min_left = solution[left]
        min_right = solution[right]
        
        if sum > 0 :
            right-=1
        elif sum < 0 :
            left+= 1
        else :
            break
    else :
        if sum > 0 :
            right-=1
        elif sum < 0 :
            left+= 1


print(min_left,min_right)
