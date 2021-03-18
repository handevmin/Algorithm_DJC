import sys

n = int(sys.stdin.readline())

memory = [1000001]*1000001
memory[1] = 0
memory[2] = 1
memory[3] = 1
for i in range(4, 1000001):
    memory[i] = memory[i-1]+1
    if i % 2 == 0:
        memory[i] = min(memory[i // 2]+1, memory[i])
    if i % 3 ==0:
        memory[i] = min(memory[i // 3]+1, memory[i])

print(memory[n])