def solution(cards1, cards2, goal):
    c1 = 0
    c2 = 0
    for i in goal:
        if c1 < len(cards1) and i == cards1[c1] :
            c1 += 1
        elif c2 < len(cards2) and i == cards2[c2] :
            c2 += 1
        else:
            return "No"
    return "Yes"