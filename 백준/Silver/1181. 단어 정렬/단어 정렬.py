import sys
input=sys.stdin.readline

arr=[]
for i in range(int(input())):
    arr.append(input().rstrip())
arr=list(set(arr))
arr.sort(key=lambda arr : (len(arr),arr))
for i in arr:print(i)