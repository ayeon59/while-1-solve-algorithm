L,C = map(int,input().split())
alphabet = sorted(list(map(str,input().split())))

alphabet_vowels = ['a','i','e','o','u']
consonants = []
vowels = []

for i in range(C):
    if alphabet[i] in alphabet_vowels :
        vowels.append(alphabet[i])
    else :
        consonants.append(alphabet[i])


ans = []
double = []
def dfs(step,start,lst,count_con,count_vow):
    if step == L:
        if count_con>=2 and count_vow>=1 :
            ans.append((lst))
        return
    
    for i in range(start,C):
        if alphabet[i] in vowels:
            dfs(step+1,i+1,lst+[alphabet[i]],count_con,count_vow+1)
        else :
            dfs(step+1,i+1,lst+[alphabet[i]],count_con+1,count_vow)
dfs(0,0,[],0,0)

for x in ans:
    print(''.join(x))