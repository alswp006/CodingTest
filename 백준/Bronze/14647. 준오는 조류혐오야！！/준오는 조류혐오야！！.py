n,m=map(int,input().split())
total=0
nine=0
arr=[]
for i in range(n):
    arr.append(list(map(str,input().split())))

for i in range(len(arr)):
    temp = 0
    for j in range(len(arr[i])):
        temp += arr[i][j].count('9')
        total += arr[i][j].count('9')
    nine = max(nine, temp)


for i in range(len(arr[0])):
    temp = 0
    for j in range(len(arr)):
        temp += arr[j][i].count('9')
    nine = max(nine,temp)

print(total - nine)