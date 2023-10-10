answer=1
n=int(input())

for i in range(1,n+1):
    answer*=i
    temp=answer%10000000
    while temp%10==0:
        temp//=10
    answer=temp

print(answer%10)