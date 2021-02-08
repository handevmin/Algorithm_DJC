import sys

c_alpha = ['c=', 'c-', 'd-', 'lj', 'nj','s=','z=']
str = sys.stdin.readline().rstrip()
indexList = []
index = -1
count =0
while True:
    index = str.find('dz=', index + 1)
    if index == -1:
        break
    else:
        count+=1
    indexList.append(index)
str = str.replace('dz=',' ')
for i in c_alpha:
    index = -1
    while True:
        index = str.find(i, index+1)
        if index == -1:
            break
        else:
            count+=1
    str = str.replace(i, ' ')
str = str.replace(' ', '')
count+=len(str)
print(count)