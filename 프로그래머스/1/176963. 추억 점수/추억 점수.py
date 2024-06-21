def solution(name, yearning, photo):
    answer = []
    d = dict()
    for i in range(len(name)):
        d[name[i]] = yearning[i]
        
    for i in photo:
        point = 0
        for person in i:
            if person in d:
                point += d[person]
        answer.append(point)
        
    return answer