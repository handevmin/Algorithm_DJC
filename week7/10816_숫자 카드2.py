import sys

his_card = int(sys.stdin.readline())
his_card_list = list(map(int, sys.stdin.readline().split()))

target_card = int(sys.stdin.readline())
target_card_list = list(map(int, sys.stdin.readline().split()))

result = [0]*target_card
index =0
his_card_list.sort()

his_card_count = {}
for i in his_card_list:
    if i not in his_card_count:
        his_card_count[i] = 1
    else:
        his_card_count[i] += 1

for i in target_card_list:
    if i > his_card_list[-1]:
        continue
    elif i < his_card_list[0]:
        continue
    else:
        left = 0
        right = len(his_card_list)
        while True:
            mid = (left + right) // 2
            if i == his_card_list[mid]:
                result[index]=his_card_count[i]
                break
            elif i > his_card_list[mid]:
                left = mid +1
            elif i < his_card_list[mid]:
                right = mid -1
            if left > right:
                break
    index += 1
print(result)