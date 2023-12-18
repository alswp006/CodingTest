alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

start, end = map(int, input().split())
arr = []
answer = []

for i in range(start, end + 1):
    temp = []
    for j in str(i):
        temp.append(alp[int(j)])
    arr.append(temp)

arr.sort()

for i in arr:
    temp = []
    for j in i:
        temp.append(str(alp.index(j)))
    answer.append(''.join(temp))

for i in range(len(answer)):
    print(answer[i], end=' ')
    if i % 10 == 9:
        print()