N = int(input())
body = []
for i in range(N):
    body.append([])
    x, y = input().split(' ')
    body[i].append(int(x))
    body[i].append(int(y))
res = []
for j in range(len(body)):
    res.append(len(body)+1)
for i in range(len(body)):
    for j in range(len(body)):
        if body[i][0] >= body[j][0] or body[i][1] >= body[j][1]:
            res[i]-=1
res = list(map(str, res))
print(' '.join(res))


