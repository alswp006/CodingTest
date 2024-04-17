n = int(input())
tall = list(map(int, input().split()))
num = [0] * n

for height, tall_person in enumerate(tall):
    temp_cnt = 0
    for j in range(len(num)):
        if num[j] == 0:
            if temp_cnt == tall_person:
                num[j] = height + 1
                break
            temp_cnt += 1

print(*num)