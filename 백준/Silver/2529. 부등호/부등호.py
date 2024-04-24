n = int(input())
arr = ''.join(input().split())
desc = 9
asc = 0
answer_min = []
answer_max = []
arr_max = arr
arr_min = arr

if arr_max[0] == ">":
    answer_max.append(desc)
    desc -= 1
else:
    answer_min.append(asc)
    asc += 1

for i in range(n):
    len_under = len(arr_max) - len(arr_max.lstrip("<"))
    len_over = len(arr_max) - len(arr_max.lstrip(">"))

    if len_under > 0:
        for i in range(desc - len_under, desc + 1):
            answer_max.append(i)
        arr_max = arr_max.lstrip("<")
        desc -= len_under + 1

        for i in range(asc, asc + len_under - 1):
            answer_min.append(i)
        arr_min = arr_min.lstrip("<")
        asc += len_under - 1

    if len_over > 0:
        for i in range(desc, desc - len_over + 1, -1):
            answer_max.append(i)
        arr_max = arr_max.lstrip(">")
        desc -= len_over - 1

        for i in range(asc + len_over, asc - 1, -1):
            answer_min.append(i)
        arr_min = arr_min.lstrip(">")
        asc += len_over + 1
else:
    if arr[-1] == ">":
        answer_max.append(desc)
    else:
        answer_min.append(asc)

print(''.join(map(str, answer_max)))
print(''.join(map(str, answer_min)))
