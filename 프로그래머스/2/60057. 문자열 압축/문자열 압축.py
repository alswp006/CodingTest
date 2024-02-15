def solution(s):
    answer = list()
    li = list(s)
    half = len(s) // 2 + 1
    
    
    for i in range(1, half + 1):
        temp = []
        temp_num = 1
        temp_answer = 0
        for j in range(0, len(s), i):
            temp.append(li[j:j+i])
        for j in range(len(temp) - 1):
            if temp[j] == temp[j+1]:
                temp_num += 1
            else:
                if temp_num == 1:
                    temp_answer += i
                else:
                    temp_answer += (len(str(temp_num))) + i
                    temp_num = 1
        else:
            if temp_num == 1:
                    temp_answer += len(temp[-1])
            else:
                temp_answer += (len(str(temp_num))) + i
                temp_num = 1
            answer.append(temp_answer)

    return min(answer)