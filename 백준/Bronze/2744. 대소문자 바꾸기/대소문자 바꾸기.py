n = input()
a = []
for x in n:
    if(x>='A' and x<='Z'):
        a.append(x.lower())
    else:
        a.append(x.upper())

print(''.join(map(str, a)))