arr=list(map(int,str(int(input()))))
if sum(arr)%3!=0:
    print(-1)
else:
    arr.sort(reverse=True)
    if arr[-1]!=0:
        print(-1)
    else:
        print(''.join(map(str,arr)))