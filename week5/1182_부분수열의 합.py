import sys


N, S = map(int,sys.stdin.readline().split())
sequence = list(map(int,sys.stdin.readline().split()))
sum = 0
count = 0

def dfs(index, sum):
    global count
    if index == N: return
    if sum + sequence[index] == S:
        count+=1
    dfs(index+1, sum)
    dfs(index+1, sum + sequence[index])

dfs(0,0)
print(count)