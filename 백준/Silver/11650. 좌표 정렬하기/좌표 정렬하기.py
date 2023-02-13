import sys
input=sys.stdin.readline

arr=[]
for i in range(int(input())):
    arr.append(input().split())
arr.sort(key=lambda arr : (int(arr[0]),int(arr[1]))) 
for i in arr:print(' '.join(i))