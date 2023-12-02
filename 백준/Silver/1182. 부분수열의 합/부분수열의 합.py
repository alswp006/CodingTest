from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer=0

for i in range(1, n + 1):
    comb = list(combinations(arr, i))
    for i in comb:
        if sum(i) == m:
            answer+=1
print(answer)