import sys

di=dict()

for i in range(int(input())):
    n=int(sys.stdin.readline())
    if not n in di:
        di[n]=1
    else:
        di[n]+=1
di = dict(sorted(di.items(), key = lambda item: item[0]))
print(max(di,key=di.get))