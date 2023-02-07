arr=[]
while True:
    arr.append(list(map(int,input().split())))
    if arr[-1]==[0,0]:break
for i in range(len(arr)-1):
    if arr[i][0]>arr[i][1]:print("Yes")
    else:print("No")