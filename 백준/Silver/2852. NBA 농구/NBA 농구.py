import sys

input = sys.stdin.readline
n = int(input())

team_time = {1: 0, 2: 0}
goal = {1: 0, 2: 0}
prev_team, prev_goal_time = map(str, input().split())
goal[int(prev_team)] += 1
prev_goal_time = int(prev_goal_time[:2]) * 60 + int(prev_goal_time[3:])

for _ in range(n - 1):
    pres_team, pres_goal_time = map(str, input().split())
    pres_goal_time = int(pres_goal_time[:2]) * 60 + int(pres_goal_time[3:])
    if goal[1] > goal[2]:
        team_time[1] += pres_goal_time - prev_goal_time
    elif goal[1] < goal[2]:
        team_time[2] += pres_goal_time - prev_goal_time
    goal[int(pres_team)] += 1
    prev_team, prev_goal_time = pres_team, pres_goal_time

pres_goal_time = 48 * 60
if goal[1] > goal[2]:
    team_time[1] += pres_goal_time - prev_goal_time
elif goal[1] < goal[2]:
    team_time[2] += pres_goal_time - prev_goal_time

team_one = str(team_time[1] // 60) if team_time[1] // 60 >= 10 else str(0) + str(team_time[1] // 60)
team_one += ":"
team_one += str(team_time[1] % 60) if team_time[1] % 60 >= 10 else str(0) + str(team_time[1] % 60)
team_two = str(team_time[2] // 60) if team_time[2] // 60 >= 10 else str(0) + str(team_time[2] // 60)
team_two += ":"
team_two += str(team_time[2] % 60) if team_time[2] % 60 >= 10 else str(0) + str(team_time[2] % 60)

print(team_one)
print(team_two)