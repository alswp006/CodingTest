from collections import deque

arr=deque(map(int,input().split()))
num=10000
data=[0]*10000
answer=0

for i in range(4):
    num=min(arr[0]*1000+arr[1]*100+arr[2]*10+arr[3],num)
    arr.append(arr.popleft())

for i in range(1111,num+1):
    #다른 수의 시계수인지 판별
    if data[i]==1:continue
    #숫자에 0이 있는지 판별
    if i%10==0:
        continue
    if i%100//10==0:
        continue
    if i%1000//100==0:
        continue
    #카운트
    answer+=1
    #현재 수의 시계수 1로 저장
    data[i]=1
    temp=deque([i//1000,i//100%10,i//10%10,i%10])
    for j in range(3):
        temp.append(temp.popleft())
        data[temp[0]*1000+temp[1]*100+temp[2]*10+temp[3]]=1

print(answer)