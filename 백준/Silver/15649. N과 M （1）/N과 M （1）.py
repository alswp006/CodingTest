from itertools import permutations  
n,m=map(int,input().split())
arr=[i+1 for i in range(n)]
answer=permutations(arr,m)
for i in answer:
    print(' '.join(map(str,i)))