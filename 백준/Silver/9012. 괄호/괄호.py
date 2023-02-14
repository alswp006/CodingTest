import sys
input=sys.stdin.readline
a=[]
for _ in range(int(input())):
    arr=input()
    answer=0
    for i in arr:
        if i=='(':answer+=1
        elif i==')':answer-=1
        if answer<0:
            answer=-1
            break
    print("YES" if answer==0 else "NO")