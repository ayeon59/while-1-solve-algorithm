n = int(input())
a = list(map(int,input().split()))
a.sort()
max_score = a[-1]
new_score = 100
for i in range(n-1):
    new_score += (a[i]/max_score)*100

print(new_score/len(a))
