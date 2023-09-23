n=int(input())
i=1
x=0
y=0

while n>=i:
    n-=i
    i+=1
if n!=0:
    x=n
    y=i+1-x
else:
    x=1
    y=i-x

print(str(y) + '/' + str(x) if i%2!=0 else str(x) + '/' + str(y))