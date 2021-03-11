import sys

M = int(sys.stdin.readline())
answer = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
entry = list(map(int, sys.stdin.readline().split()))

answer.sort()

result = []
for i in entry:
    if i > answer[-1]:
        result.append(0)
    elif i < answer[0]:
        result.append(0)
    else:
        left = 0
        right = len(answer) - 1
        while True:
            mid = (right + left )//2
            if i == answer[mid]:
                result.append(1)
                break
            elif i < answer[mid]:
                right = mid-1
            elif i > answer[mid]:
                left = mid+1
            if left > right:
                result.append(0)
                break

for i in result:
    print(i)