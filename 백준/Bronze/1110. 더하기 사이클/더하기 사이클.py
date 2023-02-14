n=int(input())
num=n
answer=0
while True:
    if num>9:
        n1=num//10
        n2=num%10
    else:
        n1=0
        n2=num
    num=(n1+n2)%10
    num+=n2*10
    answer+=1
    if num==n: break
print(answer)