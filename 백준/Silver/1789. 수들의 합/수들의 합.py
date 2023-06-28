s=int(input())
n=s
answer=0
for i in range(1,s):
    if s>=i:
        s-=i
        answer+=1
    else: break
print(answer if answer!=0 else 1)