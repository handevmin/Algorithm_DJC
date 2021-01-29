money = int(input())
money = 1000-money
change = [500,100,50,10,5,1]
count=0
for i in change:
    if money == 0:
        break
    elif money %i ==0:
        count += int(money/i)
        money=0
    elif money > i:
        count+=int(money/i)
        money-=i*int(money/i)

print(count)