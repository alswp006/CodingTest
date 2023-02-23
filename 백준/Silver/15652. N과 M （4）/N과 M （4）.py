from itertools import combinations_with_replacement
n,m=map(int,input().split())
arr=[str(i+1) for i in range(n)]
answer=combinations_with_replacement(arr,m)
for i in answer:
    print(' '.join(i))