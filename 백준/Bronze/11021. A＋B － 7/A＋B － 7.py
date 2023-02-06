n=int(input())
arr=[0]*n
for i in range(n):
    a,b=map(int,input().split())
    arr[i]=a+b
for i in range(n):
    print("Case #{0}: {1}".format(i+1,arr[i]))