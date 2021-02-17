import sys
from collections import deque

def bfs(relation, start, end, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        if start == end:
            break
        for i in relation[current]:
            if visited[i] == False:
                queue.append(i)
                distance[i] = distance[current]+1
                visited[i] = True
    if distance[end]!=0:
        return distance[end]
    else :
        return -1


n = int(sys.stdin.readline())
person1, person2 = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
relation = [[]for i in range(n+1)]
distance = [0]*(n+1)

for i in range(m):
    parent, child = map(int, sys.stdin.readline().split())
    relation[parent].append(child)
    relation[child].append(parent)

visited = [False] * (n + 1)
print(bfs(relation, person1, person2, visited))
