from collections import deque
n=int(input())
q=deque()
num=1
for i in range(1,n+1):
    q.append(i)
if i==1:
    print(1)
else:
    while True:
        x=q.popleft()
        if num%2!=0:
            num-=1
            continue
        else:
            num+=1
            q.append(x)
        if len(q)==1:break

    print(q.pop())