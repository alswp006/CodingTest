from collections import deque

def solution(queue1, queue2):
    answer = 0
    limit = len(queue1) * 3
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while True:
        if sum_q1 == sum_q2: break
        if len(queue1) == 0 or len(queue2) == 0: 
            answer = -1
            break
        if answer == limit: 
            answer = -1
            break
        elif sum_q1 < sum_q2:
            answer += 1
            temp = queue2.popleft()
            sum_q2 -= temp
            sum_q1 += temp
            queue1.append(temp)
        elif sum_q1 > sum_q2:
            answer += 1
            temp = queue1.popleft()
            sum_q2 += temp
            sum_q1 -= temp
            queue2.append(temp)
    
    return answer