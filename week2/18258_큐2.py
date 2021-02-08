import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque()
for i in range(N):
    command = sys.stdin.readline().rstrip()
    if command.find('push') != -1:
        deq.append(command.split()[1])
    elif command.find('pop') != -1:
        print(deq.popleft() if len(deq)!=0 else -1)
    elif command.find('size') != -1:
        print(len(deq))
    elif command.find('empty') != -1:
        print(0 if len(deq)!=0 else 1)
    elif command.find('front') != -1:
        print(deq[0] if len(deq)!=0 else -1)
    elif command.find('back') != -1:
        print(deq[len(deq)-1] if len(deq)!=0 else -1)
    else:
        break