x,y,z,w = map(int,input().split())
step = (z-x if z-x<w-y else w-y)
step2 = (x if x<y else y)
print(step if step<step2 else step2)