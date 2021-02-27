import sys
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

def floyd_warshall(num):
    for i in range(num):
        for j in range(num):
            for k in range(num):
                distance[i][j] = min(distance[i][j], distance[i][k]+ distance[k][j])


distance = [[INF]*(n) for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j: distance[i][j] = 0

for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    if distance[a-1][b-1] > c:
        distance[a-1][b-1] = c

floyd_warshall(5)
floyd_warshall(5)


for x in range(n):
    for y in range(n):
        if distance[x][y] == INF:
            print("inf", end=" ")
        else:
            print(distance[x][y], end=" ")
    print()