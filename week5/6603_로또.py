
while True:
    k_S = list(input().split())
    if k_S == ['0']:
        break
    k = k_S[0]
    S = k_S[1:]
    lotto = S[0:6]

    def dfs(depth, begin):
        global S
        global lotto

        # 종료조건
        if depth == 6:
            print(" ".join(lotto))
        else:
            for i in range(begin,len(S)):
                lotto[depth] = S[i]
                dfs(depth+1, i+1)

    dfs(0,0)
    print()
