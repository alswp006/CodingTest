import sys
input=sys.stdin.readline
n,m=map(str,input().split())
arr=set()
for _ in range(int(n)):
    arr.add(input().rstrip())
if m=='Y':
    print(len(arr))
elif m=='F':
    print(len(arr)//2)
elif m=='O':
    print(len(arr)//3)