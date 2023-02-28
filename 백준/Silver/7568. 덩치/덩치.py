import sys
input=sys.stdin.readline
n=int(input())
arr=[]
answer=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
for i in arr:
    num=1
    for j in arr:
        if i==j:continue
        if i[0]<j[0] and i[1]<j[1]:
            num+=1
    answer.append(num)
print(' '.join(map(str,answer)))