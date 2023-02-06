n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(str,input().split())))
for i in range(n):
    arr[i][0]=float(arr[i][0])
    for j in range(1,len(arr[i])):
        if arr[i][j]=='@':arr[i][0]*=3
        elif arr[i][j]=='%':arr[i][0]+=5
        elif arr[i][j]=='#':arr[i][0]-=7
    print("{:.2f}".format(arr[i][0]))