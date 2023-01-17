def solution(food):
    answer = []
    for i in range(len(food)):
        for j in range(0,food[i]//2):
            answer.append(str(i))
    answer.append("0")
    answer+=sorted(answer[:-1],reverse=True)
    return ''.join(answer)