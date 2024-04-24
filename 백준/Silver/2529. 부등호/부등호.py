n = int(input())
s = ''.join(input().split())
desc = 9
asc = 0
answer_min = []
answer_max = []
temp_s = s

if s[0] == ">":
    answer_max.append(desc)
    desc -= 1
else:
    answer_min.append(asc)
    asc += 1

for i in range(n):
    len_under = len(temp_s) - len(temp_s.lstrip("<"))
    len_over = len(temp_s) - len(temp_s.lstrip(">"))

    if len_under > 0:
        for i in range(desc - len_under, desc + 1):
            answer_max.append(i)

        for i in range(asc, asc + len_under - 1):
            answer_min.append(i)

        temp_s = temp_s.lstrip("<")
        desc -= len_under + 1
        asc += len_under - 1

    elif len_over > 0:
        for i in range(desc, desc - len_over + 1, -1):
            answer_max.append(i)

        for i in range(asc + len_over, asc - 1, -1):
            answer_min.append(i)

        temp_s = temp_s.lstrip(">")
        desc -= len_over - 1
        asc += len_over + 1
else:
    if s[-1] == ">":
        answer_max.append(desc)
    else:
        answer_min.append(asc)

print(''.join(map(str, answer_max)))
print(''.join(map(str, answer_min)))
