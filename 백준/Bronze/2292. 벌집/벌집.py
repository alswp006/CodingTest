num=int(input())
a=6
num-=1
answer=1
while num>0:
    num-=a
    answer+=1
    a+=6
print(answer)