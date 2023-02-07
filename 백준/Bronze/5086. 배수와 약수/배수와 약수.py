arr=[]
while True:
    arr.append(list(map(int,input().split())))
    if arr[-1]==[0,0]:break
for i in range(len(arr)-1):
    if arr[i][1]%arr[i][0]==0:
        print("factor")
    elif arr[i][0]%arr[i][1]==0:
        print("multiple")
    else :
        print("neither")