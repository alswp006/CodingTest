time=list(map(int,input().split(':')))
start=list(map(int,input().split(':')))
if time[0]>=start[0]:
    start[0]+=24
if start[2]>=time[2]:
    start[2]-=time[2]
else:
    start[1]-=1
    start[2]-=time[2]-60
if start[1]>=time[1]:
    start[1]-=time[1]
else:
    start[0]-=1
    start[1]-=time[1]-60
start[0]-=time[0]
if start[0]==24:start[0]=0
answer=[]
for i in start:
    if i <10:
        answer.append('0')
    answer.append(str(i))
    answer.append(':')
for i in range(len(answer)-1):
    print(answer[i],end='')