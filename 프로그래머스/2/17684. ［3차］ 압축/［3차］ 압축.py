def solution(msg):
    answer = []
    d = dict()
    point = 1
    while chr(point + 64) <= "Z":
        d[chr(point+64)] = point
        point += 1
        
    i = 0
    while i < len(msg):
        temp = msg[i]
        for j in range(i + 1, len(msg)):
            if temp + msg[j] in d:
                temp += msg[j]
                i += 1
            else:
                answer.append(d[temp])
                d[temp + msg[j]] = point
                point += 1
                break
        i += 1
    else : answer.append(d[temp])
            
    return answer