n=int(input())
arr=[0]*3
if n/300>0:
    arr[0]==n//300
    n%=300
if n/60>0:
    arr[1]=n//60
    n%=60
if n/10>0:
    arr[2]=n//10
    n%=10
if n==0:
    print(arr[0],end=' ')
    print(arr[1],end=' ')
    print(arr[2])
else:print(-1)