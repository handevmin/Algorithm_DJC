import sys

N = int(sys.stdin.readline())
dic = {}
count = 0
for i in range(N):
    age, name = sys.stdin.readline().split()
    age = float(age)
    if age in dic.keys():
        count+=1
        dic[age+(count*0.00001)] = name
    else:
        dic[age] = name
sortedList = sorted(dic.items())
for i in sortedList:
    print(int(i[0]), i[1])