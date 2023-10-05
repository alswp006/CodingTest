from collections import deque

n,m=map(int,input().split())
d=deque(i+1 for i in range(n))
answer=0

for i in list(map(int,input().split())):
    len_d=len(d)
    if i == d[0]:
        d.popleft()
        continue
    if d.index(i)<=len_d//2:
        while d[0] != i:
            d.append(d.popleft())
            answer+=1
        else:
            d.popleft()
    else:
        while d[0] != i:
            d.appendleft(d.pop())
            answer+=1
        else:
            d.popleft()
print(answer)