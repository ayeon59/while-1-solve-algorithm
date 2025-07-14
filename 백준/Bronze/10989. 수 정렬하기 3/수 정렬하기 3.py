import sys
input = sys.stdin.readline

n = int(input())
count = [0]*10001

for i in range(n):
    count[int(input())] += 1


for i in range(len(count)):
    for j in range(count[i]):
        print(i)
