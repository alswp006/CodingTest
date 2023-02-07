from collections import deque
n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
for i in arr:
    q=deque(i)
    answer=0
    plus=0
    while q:
        c=q.popleft()
        if c=='O':
            plus+=1
            answer+=plus
        elif c=='X':
            plus=0
    print(answer)