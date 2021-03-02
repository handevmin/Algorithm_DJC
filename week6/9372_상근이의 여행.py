import sys

nation, airplane = map(int, sys.stdin.readline().split())

node = []
for i in range(airplane):
    node.append(list(map(int, sys.stdin.readline().split())))

print(node)

