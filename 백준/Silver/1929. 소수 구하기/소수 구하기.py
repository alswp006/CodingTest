n,m=map(int,input().split())
arr=[0]*1000001
arr[1]=1
for i in range(2,int(1000000**0.5)+1):
    for j in range(2,1000000//i+1):
        arr[i*j]=1
for i in range(n,m+1):
    if arr[i]==0:print(i)