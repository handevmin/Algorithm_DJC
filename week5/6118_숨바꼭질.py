from collections import deque

N, M = map(int, input().split())
farm = {}
for i in range(M):
    a,b = map(int, input().split())
    if a not in farm:
        farm[a] = [b]
    else:
        farm[a].append(b)
    if b not in farm:
        farm[b] = [a]
    else:
        farm[b].append(a)

visited = [False]*(M+1)
distance = [0]*(M+1)
count = 0

def bfs(start):
    global visited
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        count = 0
        for i in farm[v]:
            if not visited[i]:
                count+=1
                distance[i] = distance[v]+1
                queue.append(i)
                visited[i] = True
bfs(1)

print(distance.index(max(distance)), max(distance), distance.count(max(distance)))