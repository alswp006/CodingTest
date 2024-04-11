import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    temp = [0] * 201
    team_seq = []
    team = dict()
    for i in arr:
        temp[i] += 1
        if temp[i] == 5:
            team_seq.append(i)
        if temp[i] == 6:
            team[i] = 0

    temp = [0] * 201
    num = 0

    for i in arr:
        if i not in team:
            continue
        if temp[i] == 4:
            num += 1
            continue
        team[i] += num
        temp[i] += 1
        num += 1

    min_team = set()
    min_val = min(team.values())

    for key, val in team.items():
        if min_val >= val:
            min_team.add(key)

    for i in team_seq:
        if i in min_team:
            print(i)
            break
