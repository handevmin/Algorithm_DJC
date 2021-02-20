import sys

max = 100
def visit(current):
    if current <= 2 or current >= 99: return
    if visit_number[current] > 9: return

    if current % 2 == 0:
        if (current // 2) % 2 == 0:
            token = 0
        else:
            token = 1

        opp_side_even = current-1
        upside_even = current + (100 - current) // 2 + token
        downside_even = current//2-token

        list_to_visit_even = [opp_side_even, upside_even, downside_even]

        for i in list_to_visit_even:
                if visit_number[i] == 100:
                    visit_number[i] = visit_number[current]+1
                    visit(i)
                else:
                    visit_number[i] = min(visit_number[i], visit_number[current]+1)

    else :
        if (current // 2) % 2 == 0:
            token = 1
        else:
            token = 0

        upside_odd = current + (100 - current) // 2 + token
        downside_odd = current // 2 - token

        list_to_visit_odd = [upside_odd, downside_odd]

        for i in list_to_visit_odd:

                if visit_number[i] == 100:
                    visit_number[i] = visit_number[current]+1
                    visit(i)
                else :
                    visit_number[i] = min(visit_number[i], visit_number[current]+1)


visit_number = [max for _ in range(101)]
visit_number[50] = 1
current = 50
visit(50)
print(visit_number)
while True:
    num = int(sys.stdin.readline())
    if num == 0: break
    print(visit_number[num])