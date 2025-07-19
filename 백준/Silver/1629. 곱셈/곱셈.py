def power(a, b, c):
    
    if b == 1:
        return a % c
    #더 작은 숫자로 나누기
    half = power(a, b // 2, c)
    
    #더 작은 문제가 되었으면 계산!
    if b % 2 == 0:
    #더 큰 문제를 해결하기 위해 사용
        return (half * half) % c
    else:
        return (half * half * a) % c

a, b, c = map(int, input().split())
print(power(a,b,c))
