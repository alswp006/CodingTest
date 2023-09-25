while True:
    arr=[0]*26
    str=input()
    if str=='*':break
    for i in str:
        if i>='a' and i<='z':
            arr[ord(i)-97]+=1
    for i in arr:
        if i==0:
            print('N')
            break
    else:
        print('Y')