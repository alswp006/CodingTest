int(input())
arr=list(map(int,input().split()))

for i in arr:
    if int(i**0.5)**2==i:
        print(1,end=' ')
    else:
        print(0,end=' ')