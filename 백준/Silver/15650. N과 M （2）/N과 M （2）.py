from itertools import combinations
n,m=map(int,input().split())
arr=[str(i+1) for i in range(n)]
answer=combinations(arr,m)
for i in answer:
    print(' '.join(i))