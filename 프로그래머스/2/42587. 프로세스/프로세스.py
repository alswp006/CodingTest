def solution(priorities, location):
    answer = 0
    rank = sorted(priorities, reverse = True)
    point = 0
    priority_point = 0
    while priorities[location] != -1 :
        if priorities[point] == rank[priority_point]:
            priorities[point] = -1
            priority_point += 1
            answer += 1
        point += 1
        if point == len(priorities):
            point = 0
    
        
    return answer