import sys

input = sys.stdin.readline

n,m=map(int,input().split())
arr_str=[]
dict=dict()

for i in range(n):
    a=input().rstrip()
    arr_str.append(a)
    dict[a] = i

for i in range(m):
    com = input().rstrip()
    if com[0]>='1' and com[0]<='9':
        print(arr_str[int(com)-1])
    else:
        print(dict[com]+1)