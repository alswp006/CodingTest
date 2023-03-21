n=int(input())
m=int(input())
answer=0
mi=0
for i in range(n,m+1):
    if i%(i**0.5)==0:
        answer+=i
        if mi==0:
            mi=i
print(answer if answer!=0 else -1)
if mi !=0:print(mi)