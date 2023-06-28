arr=[]
for _ in range(int(input())):
    answer=[]
    for _ in range(int(input())):
        answer.append(input().split(' '))
    arr.append(max(answer,key=lambda x:int(x[1])))
for _ in arr:print(_[0])