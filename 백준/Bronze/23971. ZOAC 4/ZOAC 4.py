h,w,n,m=map(int,input().split())
answer=0
ww=0
for i in range(0,w,m+1):
    ww+=1
for i in range(0,h,n+1):
    answer+=ww
print(answer)