n,m=map(int,input().split())
arr=[0]*(m+1)
arr[1]=1
for i in range(2,int(m**0.5)+1):
    for j in range(2,m//i+1):
        arr[i*j]=1
for i in range(n,m+1):
    if arr[i]==0:print(i)