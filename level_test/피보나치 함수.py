def fibonacci(n, zero=None, one=None):
    if n == 0:
        zero += 1
        return 0
    elif n == 1:
        one += 1
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

T = int(input())
while(T>0):
    T-=1
    n = int(input())
    print(fibonacci(n,0,0))
