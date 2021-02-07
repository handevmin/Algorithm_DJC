n = int(input())
first = n
count=0
while(1):
    n = ((n%10)*10) + (n%10 + int(n/10))%10
    count+=1
    if first%10 == n%10 and int(first/10) == int(n/10):
        break
print(count)
