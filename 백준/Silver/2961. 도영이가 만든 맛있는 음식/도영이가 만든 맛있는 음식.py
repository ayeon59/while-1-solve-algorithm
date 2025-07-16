from itertools import combinations

n = int(input())
ingredients = [list(map(int,input().split())) for _ in range(n)]
min_taste = float('inf')

for i in range(n):
    for comb in combinations(ingredients,i+1):
        sour = 1
        bitter = 0
        for x, y in comb :
            sour *= x
            bitter += y
        min_taste = min(min_taste,abs(sour-bitter))


print(min_taste)        
            