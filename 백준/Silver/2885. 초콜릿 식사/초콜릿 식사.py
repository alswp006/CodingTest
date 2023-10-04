k=int(input())
count=0
choco_min=1

while k!=1:
    choco_min*=2
    if choco_min>=k: break

print(choco_min,end=' ')
sunyoung = choco_min-k

while sunyoung!=0:
    if choco_min//2 <= sunyoung:
        sunyoung-=choco_min//2
    count+=1
    choco_min//=2

print(count)