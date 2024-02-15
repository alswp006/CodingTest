arr= [0] * (int(input()) + 1)

for i in range(2, len(arr)):
    arr[i]=arr[i-1]+1
    if i%2==0:
        arr[i]=min(arr[i],arr[i//2]+1)
    if i%3==0:
        arr[i]=min(arr[i],arr[i//3]+1)

print(arr[-1])