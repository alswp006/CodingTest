from itertools import combinations
def solution(orders, course):
    answer = []
    for j in course:
        d = dict()
        max_num = 0
        for i in orders:
            for k in list(map(''.join, combinations(sorted(list(i)), j))):
                if k in d :
                    d[k] += 1
                    max_num = max(max_num, d[k])
                else:
                    d[k] = 1
        for key, value in d.items():
            if max_num == value:
                answer.append(key)
    return sorted(answer)