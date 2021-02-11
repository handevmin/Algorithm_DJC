import sys
num =0
def visit(current):
    if current ==100:
        return
    if current == 99:
        return
    if current % 2 ==0:
        if (current // 2) % 2 == 0:
            token = 0
        else:
            token = 1

        opp_side_even = current-1
        upside_even = current + (100 - current) // 2 + token
        downside_even = current//2-token
        print(upside_even)
        if visit_number[opp_side_even]==0:
            visit(opp_side_even)
            visit_number[opp_side_even] = visit_number[current] + 1
            if visit_number[opp_side_even] != 0 and visit_number[upside_even] != 0 and visit_number[downside_even] != 0:
                return
        if upside_even <= 100 and visit_number[upside_even]==0:
            visit(upside_even)
            visit_number[upside_even] = visit_number[current] + 1
            if visit_number[opp_side_even] != 0 and visit_number[upside_even] != 0 and visit_number[downside_even] != 0:
                return
        if downside_even > 0 and visit_number[downside_even]==0:
            visit(downside_even)
            visit_number[downside_even] = visit_number[current] + 1
            if visit_number[opp_side_even] != 0 and visit_number[upside_even] != 0 and visit_number[downside_even] != 0:
                return
    else :
        if (current // 2) % 2 == 0:
            token = 1
        else:
            token = 0

        upside_odd = current + (100 - current) // 2 + token
        downside_odd = current // 2 - token
        if upside_odd <= 100 and visit_number[upside_odd] == 0:
            visit(upside_odd)
            visit_number[upside_odd] = visit_number[current] + 1
            return
        if downside_odd > 0 and visit_number[downside_odd]==0:
            visit(downside_odd)
            visit_number[downside_odd] = visit_number[current] + 1
            return

visit_number = [0 for _ in range(101)]

visit_number[50] = 1

current = 50

visit(50)

print(visit_number[75])