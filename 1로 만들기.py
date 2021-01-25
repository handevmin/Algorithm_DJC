n = int(input())
count=0
t_count=0
def test(n, t_count):
    if n==1:
        return t_count
    elif n%3==0:
        t_count+=1
        n = n/3
    elif n%2==0 and test(n-1, t_count)>=test(n/2, t_count):
        n=n/2
        t_count+=1
    else:
        n=n-1
        t_count+=1
    return test(n, t_count)

def makeone(n):
    global count
    if n==1:
        return count
    elif n%3==0:
        count+=1
        n = n/3
    elif n%2==0 and test(n-1, t_count=0)>=test(n/2, t_count=0):
        n=n/2
        count+=1
    else:
        n=n-1
        count+=1
    return makeone(n)

print(makeone(n))