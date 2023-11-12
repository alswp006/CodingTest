n,m = map(int,input().split())

arr=[]

for i in range(1, (int)(n**0.5+1)):
    if n % i == 0:
        if n // i == i:
            arr.append(i)
            continue
        arr.append(n//i)
        arr.append(i)
if len(arr) >= m:
    print(sorted(arr)[m-1])
else:
    print(0)