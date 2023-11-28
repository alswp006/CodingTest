n = int(input())
num = 1
answer=0
count=1
while n >= num:
    num *= 10
    count+=1
num/=10
count-=1
answer+=int((n-num+1)*count)
count-=1

for i in range(count-1):
    answer+=num*(count-i)*0.9
    num=int(num/10)
if n>=10:
    answer+=9
print(int(answer))