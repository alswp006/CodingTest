from collections import deque
n=input()

q=deque(n)
answer=10
while q:
    c=q.popleft()
    if len(q)>0:
        if c==q[0]:answer+=5
        else : answer+=10
print(answer)