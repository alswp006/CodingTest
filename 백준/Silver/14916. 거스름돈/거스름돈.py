answer=0
n=int(input())
five = n//5
n -= five*5

while five!=-1:
    if n%2==0:
        print(five+(n//2))
        break
    five-=1
    n+=5
else:
    print(-1)