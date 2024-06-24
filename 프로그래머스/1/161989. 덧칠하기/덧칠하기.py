from collections import deque

def solution(n, m, section):
    answer = 0
    d = deque(section)
    
    while d:
        x = d.popleft()
        answer += 1
        for i in range(x, x + m):
            if len(d) == 0: break
            if i == d[0]:
                d.popleft()
    return answer