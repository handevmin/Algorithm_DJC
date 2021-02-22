def dfs(index, lotto):
    if index == k:
        return
    dfs(index+1, lotto)
    print(S[index])
    dfs(index+1, lotto + lotto+)
k_S = list(map(int, input().split()))
k = k_S[0]
S = k_S[1:]
lotto = []
dfs(0, lotto)

