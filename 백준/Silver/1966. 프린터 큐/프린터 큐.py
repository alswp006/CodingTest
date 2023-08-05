import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n,m=map(int,input().split())
    num=deque(list(map(int,input().split())))
    target=max(num)
    answer=0
    while m>-1:
        for i in range(1,len(num)):
            if num[0]<num[i]:
                num.append(num.popleft())
                m-=1
                if m==-1:
                    m=len(num)-1
                break
        else:
            num.popleft()
            m-=1
            answer+=1
    print(answer)