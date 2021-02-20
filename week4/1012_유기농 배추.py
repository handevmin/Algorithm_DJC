import sys

def dfs(bechubat, row, col, visited, M, N):
    global connect
    visited[row][col] = True
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if nr >= 0 and nc >= 0 and nr < N and nc < M:
            if visited[nr][nc] == False and bechubat[nr][nc] == 1:
                connect +=1
                visited[nr][nc] = True
                dfs(bechubat, nr, nc, visited, M, N)

dr = [0,0,-1,1]
dc = [1,-1,0,0]
T = int(sys.stdin.readline())
for i in range(T):
    total_bechu = 0
    connect = 0

    M, N, K = map(int, sys.stdin.readline().split())
    bechubat = [[0]*(M) for i in range(N)]
    visited = [[False]*(M) for i in range(N)]

    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        bechubat[y][x] = 1
    for row_index, row in enumerate(bechubat):
        total_bechu += row.count(1)

        for col_index, val in enumerate(row):
            if bechubat[row_index][col_index] == 1 and visited[row_index][col_index] == False:
                dfs(bechubat, row_index, col_index, visited, M, N)
    print(total_bechu - connect)