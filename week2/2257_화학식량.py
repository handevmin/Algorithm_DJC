import sys
from collections import deque

str = sys.stdin.readline()
res = 0
find = None
flag = 0
deq = deque()
mul = 1
for i, val in enumerate(str):
    print(val,'일때')
    if flag != 0:
        deq.append(val)
    if val == '(':
        flag += 1
    elif val == ')':
        while flag ==0:
            flag -= 1
            deq.pop()
            deq.popleft()
        print(deq)
        if str[i+1] == '\n':
            pass
        elif int(str[i+1])>=2 and int(str[i+1])<=9:
            mul = int(str[i+1])
        for j in deq:
            if j =='H':
                res+=1*mul
            elif j == 'O':
                res+=16*mul
            elif j == 'C':
                res+=12*mul
            mul = 1
        print(res)
        deq.clear()

print(res)