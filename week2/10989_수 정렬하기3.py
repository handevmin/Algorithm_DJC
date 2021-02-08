import sys

N = int(sys.stdin.readline())
res = [0 for i in range(10001)]
for i in range(N):
    res[int(sys.stdin.readline())]+=1
for index, value in enumerate(res):
    if value == 0:
        continue
    else:
        for i in range(value):
            print(index)