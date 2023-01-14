def solution(d, budget):
    d=sorted(d)
    answer = 0
    for i in d:
        budget-=i
        answer+=1
        if budget<0:
            answer-=1
            break
    return answer