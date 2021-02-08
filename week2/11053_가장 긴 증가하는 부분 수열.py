import sys

N = int(sys.stdin.readline())
seq = list(map(int,sys.stdin.readline().split()))
count=0
lenArr = []
for i in seq:
    for j in range(i+1,seq):
        if j>i:
            count+=1
        else:
            pass
print(seq)