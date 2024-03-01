import sys
input = sys.stdin.readline

case = 1
while True:
    n = int(input())
    answer = 0
    num = 0
    if n == 0:
        break
    d = dict()
    for i in range(n):
        temp = list(input().split())
        d[temp[0]] = temp[1]

    while True:
        if len(d) <= num :
            break
        start = list(d.keys())[num]
        start_val = d[start]
        while d[start] != start:
            if d[start] in d and d[d[start]] in d:
                d[start] = d.pop(d[start])
            else:
                d.pop(start)
                break
        if start in d and d[start] == start:
            num += 1
            answer +=1
    print(case, num)
    case += 1