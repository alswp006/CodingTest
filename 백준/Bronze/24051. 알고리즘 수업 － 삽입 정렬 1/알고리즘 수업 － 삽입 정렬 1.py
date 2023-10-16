import sys

n,k = map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))
count=0

for i in range(1,len(arr)):
    temp=arr[i]
    if arr[i]>arr[i-1]:continue
    for j in range(i,0,-1):
        if temp < arr[j-1]:
            arr[j] = arr[j-1]
            count+=1
        elif temp>arr[j-1]:
            arr[j] = temp
            count+=1
            break
        if count == k:
            print(arr[j])
            exit()
    else:
        arr[0]=temp
        count+=1
print(-1)