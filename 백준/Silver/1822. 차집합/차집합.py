import sys

input=sys.stdin.readline

n,m=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=sorted(list(a-b))
if len(c)>0:
    print(len(c))
    print(' '.join([str(i) for i in c]))
else:print(0)