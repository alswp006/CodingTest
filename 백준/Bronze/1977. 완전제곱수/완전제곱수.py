a=int(input())
b=int(input())
answer=0
m=100000000
for i in range(a,b+1):
    if i%(i**0.5)==0:
        m=min(m,i)
        answer+=i
if answer==0:print(-1)
else: 
    print(answer)
    print(m)