import sys
from difflib import SequenceMatcher

N, M = map(int, sys.stdin.readline().split())

DNA_type = ['A','C','G','T']

DNA = []
for i in range(N):
    DNA.append(sys.stdin.readline().split())

count_DNA = []
for j in range(M):
    count_DNA.append([0,0,0,0])

for x in DNA:
    for y in range(M):
        if x[0][y] == 'A':
            count_DNA[y][0] +=1
        elif x[0][y] == 'C':
            count_DNA[y][1] +=1
        elif x[0][y] == 'G':
            count_DNA[y][2] +=1
        elif x[0][y] == 'T':
            count_DNA[y][3] +=1

result = []
for k in count_DNA:
    result.append(k.index(max(k)))

result = map(lambda x: DNA_type[x], result)
result = "".join(result)
print(result)
hamming_distance_sum = 0
for x in DNA:
    for y in range(M):
        if x[0][y] != result[y]:
            hamming_distance_sum+=1

print(hamming_distance_sum)

