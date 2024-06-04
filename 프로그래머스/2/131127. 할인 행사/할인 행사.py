from collections import deque

def solution(want, number, discount):
    answer = 0
    my_menu_num = {}
    for i in range(len(want)): my_menu_num[want[i]] = i
    my_num = [i for i in number]
    flag = False
    menus = deque()

    for menu in discount:
        if menu in my_menu_num:
            my_num[my_menu_num[menu]] -= 1
            menus.append(menu)
            if len(menus) == sum(number) and my_num.count(0) == len(number):
                answer += 1
            elif len(menus) > sum(number):
                my_num[my_menu_num[menus.popleft()]] += 1
                if my_num.count(0) == len(number):
                    answer += 1
            continue
            
        flag = False
        my_num = [i for i in number]
        menus = deque()

    return answer