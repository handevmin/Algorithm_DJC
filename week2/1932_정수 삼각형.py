import sys

n = int(sys.stdin.readline())
t = []
res = 0
for i in range(n):
    t.append(list(map(int,sys.stdin.readline().split())))
for i in range(n-1,1, -1):
    max = 0
    for j in range(i):
        print(t[i][j])
        c_max = t[i][j] + t[i-1][j] if t[i][j] + t[i-1][j] > t[i-1][j] + t[i][j+1] else t[i-1][j] + t[i][j+1]
        if c_max > max :
            max = c_max
            index = j
        print('max',max)
    res += max

print(res)