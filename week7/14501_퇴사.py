import sys
# 정답보기
N = int(sys.stdin.readline())
time = []
reward  = []
schedule = []
for i in range(N):
    schedule.append(list(map(int, sys.stdin.readline().split())))
    time.append(schedule[i][0])
    reward.append(schedule[i][1])
print(schedule)
print(time)
print(reward)
result = 0
# for index, duration in enumerate(time):
#     if time[index] >

memo = [0]*N
def find_maximum(period, result):
    memo[period] += reward[period]
    if period > N:
        return result

    if find_maximum(period + 1) > find_maximum(period + time[period]):
        result += reward[period]
    return memo[period]



print(find_maximum(0), 0)