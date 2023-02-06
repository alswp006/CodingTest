from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    q=deque(people)
    while q:
        if len(q)==1:
            answer+=1
            break
        light=q.popleft()
        if light+q[-1]<=limit:
            q.pop()
            answer+=1
        else:
            answer+=1
    return answer