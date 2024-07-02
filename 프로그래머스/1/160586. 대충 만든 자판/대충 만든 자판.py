def find_index(arr, num):
    for i in range(len(arr)):
        if num == arr[i]:
            return i + 1
    return -1
def solution(keymap, targets):
    answer = []
    for i in targets:
        num = 0
        for target in i:
            min_index = 10**6
            min_num = 10**6
            for key in range(len(keymap)):
                m = find_index(keymap[key], target)
                if m == -1:
                    continue
                if min_num > m:
                    min_num = m
                    min_index = key
            if min_num == 10**6:
                num = -1
                break
            num+=min_num
        answer.append(num)
        
    return answer