n = input()
dictionary = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
for x in dictionary :
    count += n.count(x)
    n = n.replace(x,"*")

n = n.replace("*","")
count += len(n)
print(count)

