n = int(input())
tall = list(map(int, input().split()))
num = [0] * (n)

for height, tall_person in enumerate(tall):
    temp_cnt = 0
    for j in range(len(num)):
        if temp_cnt == tall_person and num[j] == 0:
            num[j] = height + 1
            break
        if num[j] == 0:
            temp_cnt += 1

for i in num: print(i, end=' ')