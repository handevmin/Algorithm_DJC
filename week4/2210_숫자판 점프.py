import sys

def dfs(build_num, row, col, count):
    if count == 5:
        if build_num not in result:
            result.append(build_num)
        return

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if nr >= 0 and nc >= 0 and nr < 5 and nc < 5:
            dfs(build_num*10 + board[nr][nc], nr, nc, count+1)

board = []
for i in range(5):
    input_row = list(map(int,(sys.stdin.readline().split())))
    board.append(input_row)
dr = [0,0,-1,1]
dc = [1, -1, 0,0]
result = []
for row_index, row in enumerate(board):
    for col_index, val in enumerate(row):
        dfs(board[row_index][col_index], row_index, col_index, 0)
print(len(result))