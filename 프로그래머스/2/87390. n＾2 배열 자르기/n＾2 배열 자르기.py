def solution(n, left, right):
    answer = []
    point = 0
    for i in range(left, right + 1):
        if (i+1) % n == 0:
            answer.append(n)
        elif (i+1) % n <= (i+1) // n:
            answer.append((i+1)//n + 1)
        else :
            answer.append((i+1)%n)
        
    return answer