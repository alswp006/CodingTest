def solution(brown, yellow):
    answer = []
    for i in range(3,brown+yellow):
        if (brown+yellow)%i!=0:
            continue
        a2 = int((brown+yellow)/i)
        if (i*2)+(a2-2)*2==brown:
            return[a2,i]
    return answer