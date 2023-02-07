n=int(input())
arr=[]
for i in range(n):
    yeon,ko=0,0
    for j in range(9):
        x,y=map(int,input().split())
        yeon+=x
        ko+=y
    if yeon>ko:
        arr.append("Yonsei")
    elif yeon==ko:
        arr.append("Draw")
    else :
        arr.append("Korea")
for i in arr:
    print(i)