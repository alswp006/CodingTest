num=int(input())

arr=[i for i in range(num+1)]
answer=0
an=[]
for i in arr:
    te=[num,num-i]
    k=2
    while True:
        if te[-2]-te[-1]<0:break
        te.append(te[-2]-te[-1])
        k+=1
    if answer<k:
        answer=k
        an=te
print(answer)
for i in an:
    print(i,end=' ')