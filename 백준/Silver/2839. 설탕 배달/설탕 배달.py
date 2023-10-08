n=int(input())
answer=0

while n>0:
    if n%5==0:
        print(answer+(n//5))
        break
    answer+=1
    n-=3
else:
    if n==0:
        print(answer)
    else:
        print(-1)