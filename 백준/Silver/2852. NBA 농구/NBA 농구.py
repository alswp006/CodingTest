import sys

def cal_time(pres_time, time):
    if point[0] > point[1]:
        win_time[0] += time - pres_time
    elif point[0] < point[1]:
        win_time[1] += time - pres_time

n = int(input())
point = [0, 0]
win_time = [0, 0]
pres_time = 0

for i in range(n):
    team, time = map(str, sys.stdin.readline().split())
    hour, minute = map(int, time.split(":"))
    time = hour * 60 + minute
    cal_time(pres_time, time)
    point[int(team) - 1] += 1
    pres_time = time

cal_time(pres_time, 48*60)

print(f'{win_time[0] // 60:02}:{win_time[0] % 60:02}')
print(f'{win_time[1] // 60:02}:{win_time[1] % 60:02}')