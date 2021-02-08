import sys

x, y = sys.stdin.readline().split()
x, y = int(x), int(y)

if x==y:
    print(x)
    print(x)

elif x%y==0 or y%x==0:
    print(x if x<y else y)
    print(x if x>y else y)

else:
    m = int(x ** 0.5)
    n = int(y ** 0.5)
    min = m if m>n else n
    gcd = 1
    for i in range(2,min+1):
        while x%i==0 and y%i==0:
            x=x/i
            y=y/i
            gcd = gcd*i
    print(gcd)
    print(int(gcd*x*y))
