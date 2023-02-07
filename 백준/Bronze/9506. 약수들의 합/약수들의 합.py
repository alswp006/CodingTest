arr=[]
while True:
    arr.append(int(input()))
    if arr[-1]==-1:
        arr.remove(-1)
        break
for i in arr:
    dcm=[1]
    for j in range(2,int(i**0.5+1)):
        if i%j==0:
            dcm.append(j)
            dcm.append(int(i/j))
    dcm.sort()
    if i-sum(dcm)==0:
        print("{0} = {1}".format(i,dcm[0]),end='')
        for k in range(1,len(dcm)):
            print(" + {0}".format(dcm[k]),end='')
    else:print("{0} is NOT perfect.".format(i),end='')
    print()