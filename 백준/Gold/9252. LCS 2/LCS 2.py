s1 = input()
s2 = input()
arr = [[''] * len(s1) for _ in range(len(s2))]

flag = False
for i in range(len(s1)):
    if s2[0] == s1[i]:
        flag=True
    if flag:
        arr[0][i] = s2[0]

flag = False
for i in range(len(s2)):
    if s1[0] == s2[i]:
        flag = True
    if flag:
        arr[i][0] = s1[0]

for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if s2[i] == s1[j]:
            arr[i][j] = arr[i - 1][j - 1] + s1[j]
        else:
            if len(arr[i - 1][j]) >= len(arr[i][j - 1]):
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = arr[i][j - 1]

print(len(arr[-1][-1]))
print(arr[-1][-1])