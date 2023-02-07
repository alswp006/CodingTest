arr=list(map(int,input().split()))
arr.sort()
if arr[2]==arr[1] and arr[1]==arr[0]:
    print(10000+arr[2]*1000)
elif arr[2]==arr[1] or arr[1]==arr[0]:
    print(1000+100*arr[1])
else:
    print(100*arr[2])