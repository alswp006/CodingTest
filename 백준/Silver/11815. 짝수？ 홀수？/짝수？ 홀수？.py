from math import sqrt
int(input())
arr=list(map(int,input().split()))

for i in arr:
    num=int(sqrt(i))
    if i//num==num and i%num ==0:
        print(1,end=' ')
    else:
        print(0,end=' ')