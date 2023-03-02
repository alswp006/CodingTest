arr=list(map(str,input()))
num=0

for i in range(1,100000):
    n=list(map(int,str(i)))
    for ii in n:
        a=0
        if num!=len(arr):
            if ii == int(arr[num]):
                num+=1
                a+=1
                continue
            if num==len(arr):
                break
            if a>0 and ii !=int(arr[num]):
                break
    if num==len(arr):
        print(i)
        break