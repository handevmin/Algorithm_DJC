import sys

memory_zero = [0]*41
memory_zero[0] = 1
memory_zero[1] = 0

memory_one = [0]*41
memory_one[0] = 0
memory_one[1] = 1
T = int(sys.stdin.readline())
for i in range(2, 41):
    memory_zero[i] = memory_zero[i-1] + memory_zero[i-2]
    memory_one[i] = memory_one[i - 1] + memory_one[i - 2]
for i in range(T):
    n = int(sys.stdin.readline())
    print(memory_zero[n], memory_one[n])
