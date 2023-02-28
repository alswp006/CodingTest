n=int(input())
sc=list(map(int,input().split()))
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==1:
        for i in range(b-1,len(sc),b):
            if sc[i]==0:sc[i]=1
            else: sc[i]=0
    if a==2:
        x=1
        b-=1
        if sc[b]==0:sc[b]=1
        else: sc[b]=0
        while True:
            if b-x<0 or b+x>=len(sc):break
            if sc[b-x]!=sc[b+x]:break
            if sc[b-x]==0:sc[b-x]=1
            else: sc[b-x]=0
            if sc[b+x]==0:sc[b+x]=1
            else: sc[b+x]=0
            x+=1
for i in range(len(sc)):
    print(sc[i],end=' ')
    if (i+1)%20==0:print()