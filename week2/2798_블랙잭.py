from itertools import combinations

n, m = input().split()
card = input().split()
card = list(map(int, card))
combi = list(combinations(card, 3))
min = 300000
for j in range(len(combi)):
    _sum = sum(combi[j])
    if int(m)-_sum>=0 and int(m)-_sum<min:
        res = _sum
        min = int(m)-_sum
print(res)