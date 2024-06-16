from itertools import permutations

def calcul(n1, n2, s):
    n1, n2 = int(n1), int(n2)
    if s == "-":
        return n1 - n2
    elif s == "+":
        return n1 + n2
    elif s == "*":
        return n1 * n2
def solution(expression):
    answer = 0
    temp = ''
    num = []
    my_iterators = []
    for i in expression:
        if i not in "+-*":
            temp += i
            continue
        num.append(temp)
        temp = ''
        my_iterators.append(i)
    else:
        num.append(temp)
        
    case_num = list(map(list, permutations(["+", "-", "*"], 3)))
    for case in case_num:
        copy_num = num.copy()
        copy_my_iterators = my_iterators.copy()
        temp = 0
        for iterator in case:
            cal_cnt = 0 
            for i in range(len(copy_my_iterators)):
                if iterator == copy_my_iterators[i]:
                    copy_num[i + 1] = calcul(copy_num[i], copy_num[i+1], iterator)
                    copy_num[i] = "@"
                    copy_my_iterators[i] = "@"
                    cal_cnt += 1
            for i in range(cal_cnt):
                copy_num.remove("@")
                copy_my_iterators.remove("@")
        if copy_num[0] < 0 : copy_num[0] *= -1
        answer = max(answer, copy_num[0])
    return answer