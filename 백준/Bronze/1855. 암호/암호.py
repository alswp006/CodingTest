n = int(input())
arr = list(input())
char = []

for i in range(0, len(arr), n):
    char.append(arr[i : i + n])
for i in range(1,len(char),2):
    char[i].reverse()

for i in range(len(char[0])):
    for j in range(len(char)):
        print(char[j][i],end='')