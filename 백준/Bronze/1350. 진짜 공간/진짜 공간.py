n=int(input())
arr=list(map(int,input().split()))
clu=int(input())
num=0

for i in arr:
    if i == 0 : continue
    else:
        if i % clu == 0 :
            num += i // clu
        else :
            num += i // clu + 1
print(num*clu)