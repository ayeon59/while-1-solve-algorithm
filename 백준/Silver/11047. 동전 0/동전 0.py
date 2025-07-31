import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
money = 0
cnt = 0 
result = 0

for i in range(n-1,-1,-1) :
    #사용할 수 있는 코인이 아니면
    if money == k :
        break
    if (k-money) // coin[i] == 0:
        continue
    cnt = (k-money)//coin[i]
    
    money += coin[i]*cnt
    result += cnt

print(result)
    



