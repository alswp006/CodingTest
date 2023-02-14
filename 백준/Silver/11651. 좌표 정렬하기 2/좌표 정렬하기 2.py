import sys
input=sys.stdin.readline

arr=[]
for i in range(int(input())):
    arr.append(input().split())
arr.sort(key=lambda arr : (int(arr[1]),int(arr[0]))) 
for i in arr:print(' '.join(i))