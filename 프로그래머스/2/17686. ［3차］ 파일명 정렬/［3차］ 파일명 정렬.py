def solution(files):
    answer = []
    an_answer = []
    for i in files:
        flag = 0
        temp = [[],[]]
        for j in range(len(i)):
            if flag == 0 and "0"<= i[j] <="9":
                flag +=1
            elif flag == 1 and not "0"<= i[j] <="9":
                temp.append(i[j:])
                break
            temp[flag].append(i[j])
        answer.append(temp)
    answer.sort(key = lambda x : (''.join(x[0]).upper(), int(''.join(x[1]))))
    
    for i in answer:
        an_answer.append(''.join(i[0]) + ''.join(i[1]))
        if len(i) > 2:
            an_answer[-1] += i[2]
    return an_answer