n,a,b= map(int,input().split())
answer=1

while True:
    ma=max(a,b)
    mi=min(a,b)
    if ma%2==0 and ma-mi==1:
        break
    a = a//2+(a%2)
    b= b//2+(b%2)
    answer+=1
print(answer)