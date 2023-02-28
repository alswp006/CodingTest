import sys

input=sys.stdin.readline
n=int(input().rstrip())
arr=list(map(int,input().split()))
money=int(input().rstrip())
arr.sort()
num=0
for i in range(n):
    if money//(n-i)>=arr[i]:
        money-=arr[i]
    else:
        money=money//(n-i)
        break
    num+=1

print(money if money<=arr[-1] and num!=n else arr[-1])