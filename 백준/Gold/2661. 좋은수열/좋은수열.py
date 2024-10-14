def choose_num(result, count, result_list):
    for i in range(1, count // 2 + 1):
        if result_list[-i:] == result_list[-2 * i:-i]:
            return
    if count == target:
        print("".join(map(str, result_list)))
        exit(0)
    for i in range(1, 4):
        result_list.append(i)
        choose_num(result * 10 + i, count + 1, result_list)
        result_list.pop()


target = int(input())
choose_num(0, 0, [])