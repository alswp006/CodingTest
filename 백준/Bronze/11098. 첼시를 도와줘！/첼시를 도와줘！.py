import sys
input=sys.stdin.readline

for _ in range(int(input())):
    arr=[]
    for i in range(int(input())):
        arr.append(list(map(str,input().split())))
    arr.sort(key=lambda x : int(x[0]))
    print(arr[-1][-1])