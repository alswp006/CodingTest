answer=0
num=-1

for i in range(5):
    temp=sum(map(int,input().split()))
    if num< temp:
        num=temp
        answer=i+1
print(answer,num)