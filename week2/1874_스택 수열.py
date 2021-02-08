import sys

n = int(sys.stdin.readline())
seq = []
stack = []
res = []
cnt =0
pre = 0
flag = 1
for i in range(n):
    seq.append(int(sys.stdin.readline()))

for i in seq:
    if flag ==0 : break
    else:
        if i < pre:
            while True:
                res.append('-')
                pre = stack.pop()
                if pre == i:
                    break
        else:
            while True:
                if cnt > n:
                    flag=0
                    res.clear()
                    res.append('NO')
                    break
                if cnt == i:
                    res.append('-')
                    pre = stack.pop()
                    break
                res.append('+')
                cnt+=1
                stack.append(cnt)
            pre = cnt

for i in res:
    print(i)
