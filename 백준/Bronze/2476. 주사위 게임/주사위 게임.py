n=int(input())
price=[]
for i in range(n):
    arr=[]
    arr=list(map(int,input().split()))
    arr.sort()
    if arr[2]==arr[1] and arr[1]==arr[0]:
        price.append(10000+arr[2]*1000)
    elif arr[2]==arr[1] or arr[1]==arr[0]:
        price.append(1000+100*arr[1])
    else:
        price.append(100*arr[2])
print(max(price))