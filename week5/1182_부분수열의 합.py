import sys

N, S = map(int,sys.stdin.readline().split())
sequence = list(map(int,sys.stdin.readline().split()))
sum = 0
count = 0

def dfs(index, sum):
    global count
    # N까지 모두 돌았을 때 종료
    if index == N: return
    print(index, sum, sum + sequence[index])

    if sum + sequence[index] == S:
        count+=1


    dfs(index+1, sum) # 여기서 0,1,2,3,4 순으로 원소가 한 개일 때 검사 후
    dfs(index+1, sum + sequence[index]) # 4번부터 반환되면서 다시 윗 줄 dfs로 들어가면서
    # 3일 때 17번 줄: (3,4),
    # 2일 때 17번 줄에서의 16번 줄 재귀: (2,3), (2,4),
    # 2일 때 17번 줄: (2,3,4),
    # 1일 때 17번 줄에서의 16번 줄 재귀: (1,2), (1,3), (1,4),
    # 1일 때 17번 줄:                        (1,3,4),
    #                                (1,2,3), (1,2,4)
    #                                (1,2,3,4)
    # 0일 때 17번 줄에서의 16번 줄에서의 16번 줄 재귀: (0,1), (0,2), (0,3), (0,4)
    # 0일 때 17번 줄에서의 16번 줄에서의 17번 줄 재귀:               (0,3,4),
    #                                                   (0,2,3), (0,2,4)
    #                                                            (0,2,3,4)
    #                                            (0,1,2), (0,1,3), (0,1,4)
    #                                                     (0,1,3,4)
    #                                            (0,1,2,3), (0,1,2,4)
    #                                            (0,1,2,3,4)

dfs(0,0)
print(count)