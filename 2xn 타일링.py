n = int(input())
def recur(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return recur(n-1)+1
print(recur(n))
