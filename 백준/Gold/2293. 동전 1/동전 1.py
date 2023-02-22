n,m=map(int,input().split())
type=[int(input()) for i in range(n)]
d=[0 for i in range(m+1)]
d[0]=1
for i in type:
    for j in range(i,m+1):
        d[j]+=d[j-i]
print(d[m])