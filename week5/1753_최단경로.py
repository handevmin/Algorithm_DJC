import sys
import heapq
INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for i in range(V+1)]
visited = [False] * (V+1)
distance = [INF]*(V+1)

for i in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

print(graph)
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    print(queue)
    distance[start] = 0
    while queue:
        print(queue)
        dist, current = heapq.heappop(queue)
        if distance[current] < dist:
            continue
        for i in graph[current]:
            print(i)
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

for d in range(1, V+1):
    if distance[d] == INF:
        print("INF")
    else:
        print(distance[d])