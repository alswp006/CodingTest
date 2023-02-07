answer=[]
while True:
    x,y=map(int,input().split())
    if x==0 and y==0:break
    answer.append(x+y)
for i in answer:print(i)