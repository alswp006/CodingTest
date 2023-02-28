import sys
input=sys.stdin.readline
n,m=map(str,input().split())
arr=[]
for _ in range(int(n)):
    arr.append(input().rstrip())
arr=list(set(arr))
if m=='Y':
    print(len(arr))
elif m=='F':
    print(len(arr)//2)
elif m=='O':
    print(len(arr)//3)