n = int(input())
a = set()
for _ in range(n):
    a.add(input())
a = list(a)
a.sort()
a.sort(key=lambda x: len(x))

for x in a:
    print(x) 
