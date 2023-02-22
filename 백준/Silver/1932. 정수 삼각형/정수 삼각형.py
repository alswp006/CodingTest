import sys
input=sys.stdin.readline
arr=[]
for i in range(int(input())):
    arr.append(list(map(int,input().split())))
for i in range(len(arr)-2,-1,-1):
    for j in range(len(arr[i])):
        arr[i][j]=max(arr[i+1][j],arr[i+1][j+1])+arr[i][j]
print(arr[0][0])