x,y,n,m=map(int,input().split())
a,b=0,0
answer=0
if 2*n>=m:
        answer+=min(x,y)*m
        a,b=min(x,y),min(x,y)
if n<m:
    answer+=((x-a)+(y-b))*n
else:
    if (x-a)%2==0:
        answer+=(x-a)*m
    else:
        answer+=(x-a-1)*m
        answer+=n
    if (y-b)%2==0:
        answer+=(y-b)*m
    else:
        answer+=(y-b-1)*m
        answer+=n
print(answer)