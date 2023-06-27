a,b,c=map(int,input().split())
c+=(int(input()))
if c>=60:
    b+=c//60
    c=c%60
if b>=60:
    a+=b//60
    b=b%60
if a>=24: a=a%24
print(a,b,c)