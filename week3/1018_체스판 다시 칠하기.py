sol_1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],]

sol_2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],]

def count_renew(input_board, sol, min):
    output= []
    cnt = 0
    for i in range(8):
        output.append(list(map(lambda x, y: 1 if x == y else 0, input_board[i], sol[i])))
        cnt += output[i].count(1)
    if cnt < min:
        min = cnt
    return min

n, m = map(int, input().split())
input_board = []
min = 2500
for i in range(n):
    input_board.append(list(input()))
for i in range(n-7):
    for j in range(m-7):
        min = count_renew([row[j:j+8] for row in input_board[i:i+8]], sol_1, min)
        min = count_renew([row[j:j+8] for row in input_board[i:i+8]], sol_2, min)
print(min)
