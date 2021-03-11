import sys

T = int(sys.stdin.readline())
for k in range(T):
    nation, airplane = map(int, sys.stdin.readline().split())
    count =0
    node = []
    for i in range(airplane):
        a, b = map(int, sys.stdin.readline().split())
        if a not in node or b not in node:
            count +=1
            if a not in node:
                node.append(a)
            if b not in node:
                node.append(b)
        print(node)
    print(count)
