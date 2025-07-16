import math

a,b,v = map(int,input().split())
day = 1
v = v-a
day += math.ceil(v / (a-b))
print(day)