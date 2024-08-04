html = list(input())

point, end_point = 6, len(html) - 8
answer = []


def slice_title(point):
    temp = ""
    while html[point] != "\"":
        temp += html[point]
        point += 1
    answer.append("title : " + temp)
    return point + 1

def slice_p_tag(point):
    temp = ""
    space_flag = False
    while True:
        if html[point] == "<":
            if html[point + 1] == "/" and html[point + 2] == "p" and html[point + 3] == ">":
                break
            point = slice_p_in_tag(point)
            continue
        if not space_flag:
            temp += html[point]
            space_flag = html[point] == " "
        else:
            if html[point] != " ":
                temp += html[point]
                space_flag = False
        point += 1
    answer.append(temp)

    return point + 3

def slice_p_in_tag(point):
    while html[point] != ">":
        point += 1
    return point + 1

div_flag = False

while point <= end_point:
    if html[point] == "<" and html[point + 1] != "/":
        if not div_flag:
            div_flag = True
            point = slice_title(point + 12)
        else:
            point = slice_p_tag(point + 3)
    else:
        div_flag = False
    point+=1

for i in answer:
    print(i)