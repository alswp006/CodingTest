for i in range(int(input())):
    str=input()
    if str[0]>='a' and str[0]<='z':
        print(str.replace(str[0],chr(ord(str[0])-32),1))
    else:
        print(str)