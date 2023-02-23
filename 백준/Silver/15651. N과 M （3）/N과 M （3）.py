from itertools import product
n,m=map(int,input().split())
arr=[str(i+1) for i in range(n)]
answer=product(arr,repeat=m)
for i in answer:
    print(' '.join(i))