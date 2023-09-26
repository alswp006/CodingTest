num=int(input())
fac=1
answer=0
for i in range(num,0,-1):
    fac*=i
while fac%10==0:
    if fac<10:
        break
    answer+=1
    fac//=10
print(answer)