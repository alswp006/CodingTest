arr = []
count = 0

for _ in range(int(input())):
    arr.append(list(map(int, input().split())))
check = [0 for i in range(arr[-1][0] + 1)]

arr.sort(key=lambda x: x[2], reverse=True)

for i in arr:
    if check[i[0]] == 2: continue
    print(i[0],i[1])
    count+=1
    check[i[0]] += 1
    if count == 3:
        break