brackets = input().strip()
stack = []

for x in brackets:
    if x == '(' or x == '[':
        stack.append(x)
    elif x == ')':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * temp)
                break
            elif type(top) == int:
                temp += top
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()
    elif x == ']':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            elif type(top) == int:
                temp += top
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()
    else:
        print(0)
        exit()

if all(type(s) == int for s in stack):
    print(sum(stack))
else:
    print(0)
