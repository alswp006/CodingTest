n=int(input())
arr=[0 for _ in range(n+1)]
arr[1]=1
if n>1:arr[2]=2
for i in range(3,len(arr)):
    arr[i]=(arr[i-1]+arr[i-2])%15746
print(arr[n])