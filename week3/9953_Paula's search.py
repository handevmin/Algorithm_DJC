
num = -1
while True:
    num = int(input())
    if num == 0 : break
    position = [50]
    current = 0
    token = 0
    while True:
        if num %2 !=0:
            token = 1
        if num == position[current]-token:
            current += 1 + token
            break
        if num < position[current]:
            if num < min(position) :
                if position[current] == 4:
                    position.append(2)
                elif position[current] ==6:
                    position.append(4)
                elif (position[current] // 2) % 2 == 0:
                    position.append((position[current]) // 2)
                else:
                    position.append((position[current]-2)//2)
            else :
                gap = min(list(map(lambda x: abs(x-num), position[:-1])))
                previous = num - gap
                if ((previous+position[current])//2) %2 !=0:
                    position.append((previous + position[current]) // 2-1)
                else:
                    position.append((previous + position[current])//2)
        elif num > position[current]:  # 올라가야 할 때
            if num > max(position) :
                if position[current] == 98:
                    position.append(100)
                elif position[current] == 96:
                    position.append(98)
                elif ((position[current]+100)//2)%2 == 0:
                    position.append((position[current]+100)//2)
                else:
                    position.append((position[current]+100+2)//2)
            else:
                gap = min(list(map(lambda x: abs(x-num), position[:-1])))
                previous = num + gap
                if ((previous+position[current])//2) %2 !=0:
                    position.append((previous + position[current]) // 2-1)
                else:
                    position.append((previous+position[current])//2)
        current+=1
    print(current)
