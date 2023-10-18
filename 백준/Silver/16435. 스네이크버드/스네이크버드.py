n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
for i in arr:
    if i<=m:m+=1
    else:break
print(m)