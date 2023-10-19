di=dict()
answer=0
answer_list=[]

for i in range(8):
    di[i+1]=int(input())
di = sorted(di.items(), key=lambda x:x[1])
for i in range(3,8):
    answer+=di[i][1]
    answer_list.append(di[i][0])
answer_list.sort()
print(answer)
for i in answer_list:
    print(i,end=' ')