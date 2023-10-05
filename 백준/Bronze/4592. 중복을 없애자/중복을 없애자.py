while True:
    arr=list(map(int,input().split()))
    if arr[0]==0:break
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            if i==1:
                print(arr[i],end=' ')
            continue
        else:
            print(arr[i],end=' ')
    print('$')