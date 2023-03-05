n=int(input())
arr=list(map(int,input().split()))
arr.sort()
num=arr[0]+arr[-1]
for i in range(n):
    num=min(num,arr[i]+arr[-i-1])
print(num)