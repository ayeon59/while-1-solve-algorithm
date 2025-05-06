import sys
inp = sys.stdin.readline

Group = 1
while True:
    num = int(inp())
    cnt = 0
    people=[]
    if not num : break
    for _ in range(num): #한사람 한사람 확인
        people.append(input().split())
    print(f"Group {Group}")
    for j in range(num): 
        for i in range(1,num):
            if people[j][i]=='P':
                continue
            else:
                cnt = 1
                p1 = people[(j-i)%num][0]
                p2 = people[j][0]
                print(f"{p1} was nasty about {p2}")
    if(cnt==0):
        print('Nobody was nasty')
    Group += 1
    print()



