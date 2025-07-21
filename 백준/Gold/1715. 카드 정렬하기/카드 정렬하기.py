#결국 더하는 횟수는 정해짐 n-1번으로
#작은 숫자에서 여러번 더하는게 이득 
import sys
import heapq
input = sys.stdin.readline

pq = []
final_sum = 0

card_num = int(input())
for _ in range(card_num):
    heapq.heappush(pq,int(input()))

for _ in range(card_num-1):
    card_sum = heapq.heappop(pq) + heapq.heappop(pq)
    final_sum += card_sum
    heapq.heappush(pq,card_sum)
print(final_sum)


