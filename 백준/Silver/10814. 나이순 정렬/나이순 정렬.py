import sys

arr=[]

for i in range(int(input())):
    a,b=map(str,sys.stdin.readline().split())
    arr.append([int(a),b])
arr.sort(key = lambda x:x[0])
for i in arr:
    print(' '.join(map(str,i)))