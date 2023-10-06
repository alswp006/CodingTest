import sys

cent=[25,10,5,1]
for i in range(int(sys.stdin.readline())):
    money=int(sys.stdin.readline())
    for j in cent:
        print(money//j,end=' ')
        money%=j
    print()