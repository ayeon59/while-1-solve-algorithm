now_hour,now_second = map(int,input().split())
time = int(input())

now_hour += time//60 
now_second += time%60

if now_second >= 60 :
    now_hour += 1
    now_second -= 60
 
if now_hour >=24:
    now_hour -=24
    
print(now_hour,end=" ")
print(now_second)