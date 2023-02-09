n=int(input())
d=[0]*(n+1)

if n==1:d[1]=1
elif n==2:d[2]=1
else:    
    d[1]=1
    d[2]=1
    for i in range(3,n+1):
        d[i]=sum(d[1:i-1])+1
print(d[n])