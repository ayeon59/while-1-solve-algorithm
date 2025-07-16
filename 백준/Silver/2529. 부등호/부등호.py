from itertools import permutations

n = int(input())
comparison = list(input().split())
answer = []
digits = [i for i in range(10)]

for perm in permutations (digits,n+1):
    
    perm = list(perm)
    isCorrect = True
    for i in range(n):
        if isCorrect :
            if comparison[i] == "<":
                if perm[i] < perm[i+1] :
                    continue
                else :
                    isCorrect = False
            else :
                if perm[i] > perm[i+1] :
                    continue
                else :
                    isCorrect = False
    if(isCorrect) : 
        answer.append(perm)

print(''.join(map(str, answer[-1])))
print(''.join(map(str, answer[0])))


