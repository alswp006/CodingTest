import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
comb = list(combinations([i for i in range(n)] ,n//2))
answer = 100000000

for i in range(len(comb) // 2):
    team_start = 0
    team_link = 0
    for j in combinations(comb[i],2):
        team_start += arr[j[0]][j[1]] + arr[j[1]][j[0]]
    for k in combinations(comb[len(comb) - i - 1], 2):
        team_link += arr[k[0]][k[1]] + arr[k[1]][k[0]]
    answer = min(answer, max(team_start, team_link) - min(team_start, team_link))

print(answer)