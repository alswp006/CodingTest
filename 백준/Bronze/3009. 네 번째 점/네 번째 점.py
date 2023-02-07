arr1=[]
arr2=[]
for i in range(3):
    x,y=(map(int,input().split()))
    arr1.append(x)
    arr2.append(y)
x,y=0,0
arr1.sort()
arr2.sort()
x=sum(arr1)-arr1[1]*2
y=sum(arr2)-arr2[1]*2
print(x)
print(y)