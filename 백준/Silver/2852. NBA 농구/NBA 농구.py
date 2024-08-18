import sys

n = int(input())
point = [0, 0]
win_time = [0, 0]
pres_time = 0

for i in range(n):
    team, time_str = map(str, sys.stdin.readline().split())
    time = int(time_str[:2]) * 60 + int(time_str[3:])
    win_time[point[0] < point[1]] += time - pres_time if point[0] != point[1] else 0
    point[int(team) - 1] += 1
    pres_time = time
win_time[point[0] < point[1]] += 48 * 60 - pres_time if point[0] != point[1] else 0

print(f'{win_time[0] // 60:02}:{win_time[0] % 60:02}')
print(f'{win_time[1] // 60:02}:{win_time[1] % 60:02}')
