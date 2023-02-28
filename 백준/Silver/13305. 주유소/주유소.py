n=int(input())
dt=list(map(int,input().split()))
city=list(map(int,input().split()))
fee=city[0]*dt[0]
c=city[0]
for i in range(1,len(city)-1):
    if city[i]<c:
        c=city[i]
        fee+=c*dt[i]
    else:
        fee+=c*dt[i]
print(fee)