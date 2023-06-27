for i in range(int(input())):
    arr=list(map(str,input().split()))
    arr[0]=float(arr[0])
    for j in range(1,len(arr)):
        if arr[j]=='@': arr[0]*=3
        elif arr[j]=='%': arr[0]+=5
        elif arr[j]=='#': arr[0]-=7
    print("{:.2f}".format(arr[0]))