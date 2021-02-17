import sys

def dfs(graph, vertex, visited):
    visited[vertex] = True
    global count_of_hack
    count_of_hack += 1
    if vertex in graph:
        for i in graph[vertex]:
            if not visited[i]:
                dfs(graph, i, visited)

N, M = map(int, sys.stdin.readline().split())
graph = {}
count_of_hack_list = {}
for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

for i in graph:
    count_of_hack = 0
    visited = [False] * (N + 1)
    dfs(graph, i, visited)
    count_of_hack_list[i] = count_of_hack
max_hack = max(count_of_hack_list.values())
max_hack_list = sorted([k for k, v in count_of_hack_list.items() if v == max_hack])
for i in max_hack_list:
    print(i, end = " ")