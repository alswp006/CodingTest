import sys

n,k=map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))
arr_sort=sorted(arr)
count=0

while arr_sort:
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == arr_sort[-1] :
            a, b = arr.pop(), arr_sort.pop()
            if a==b:continue
            else:
                count+=1
                arr[i]=a
                if count==k:
                    print(a,b)
                    exit()
print(-1)