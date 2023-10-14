import sys

arr=[]

for i in range(int(input())):
    arr.append(sys.stdin.readline().rstrip())
arr.sort(key = lambda x:int(x.split()[0]))
for i in arr:
    print(''.join(map(str,i)))