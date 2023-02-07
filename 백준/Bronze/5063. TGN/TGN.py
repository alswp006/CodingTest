n=int(input())
answer=[]
for i in range(n):
    a,b,c=map(int,input().split())
    answer.append(b-a-c)
for i in answer:
    if i>0:
        print("advertise")
    elif i==0:
        print("does not matter")
    else : 
        print("do not advertise")