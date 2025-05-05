n = int(input())
a = []
for _ in range(n):
    n = input()
    a.append(n)
b = list(set(a))   
b.sort(key=lambda x: (len(x), x))
for x in b:
    print(x)
