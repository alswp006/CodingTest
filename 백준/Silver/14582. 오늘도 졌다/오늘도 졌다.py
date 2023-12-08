t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))
t1_point = 0
t2_point = 0

for i in range(len(t1)):
    t1_point += t1[i]

    if t1_point > t2_point:
        print("Yes")
        exit()

    t2_point += t2[i]

print("No")