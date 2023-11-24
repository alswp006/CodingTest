import sys

input = sys.stdin.readline

n = int(input())
info = list(map(int,input().split()))

jun = [0, n]
sung = [0, n]
flag=0

for i in info:
    if i <= jun[1]:
        jun[0] += jun[1]//i
        jun [1] %= i

for i in range(1, len(info)):
    if info[i-1]<info[i]:
        flag+=1
        if flag <= 0:
            flag=1
    elif info[i-1]>info[i]:
        flag-=1
        if flag >= 0:
            flag=-1
    if flag == 3:
        if sung[0] != 0 :
            flag = 0
        sung[1] += sung[0] * info[i]
        sung[0] = 0
    elif flag == -3:
        if sung[0] != 0 :
            flag = 0
        sung[0] += sung[1] // info[i]
        sung[1] %= info[i]
        flag=0

sung_money = sung[0] * info[-1] + sung[1]
jun_money = jun[0] * info[-1] + jun[1]

if sung_money > jun_money:
    print("TIMING")
elif sung_money < jun_money:
    print("BNP")
else :
    print("SAMESAME")