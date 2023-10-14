import sys

n,k=map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))
arr_sort=sorted(arr)
count=0

while arr_sort:
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == arr_sort[-1] :
            if i == len(arr)-1:
                arr.pop()
                arr_sort.pop()
            else:
                count+=1
                arr[i],arr[-1] = arr[-1],arr[i]
                a,b=arr[i],arr_sort.pop()
                arr.pop()
                if count==k:
                    print(a,b)
                    exit()
print(-1)