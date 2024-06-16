move = [(-1,0), (0,1), (1,0), (0,-1)]

def O(x, y, arr):
    temp = 0
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:continue
        if arr[nx][ny] == "P":
            temp += 1
    return True if temp < 2 else False
        
def P(x, y, arr):
    temp = 0
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:continue
        if arr[nx][ny] == "P":
            return False
        elif arr[nx][ny] == "O":
            if not O(nx, ny, arr):
                return False
    return True

def solution(places):
    answer = []
    
    for place in places:
        flag = True
        for x in range(len(place)):
            for y in range(len(place[x])):
                if place[x][y] == "P":
                    flag = P(x, y, place)
                if not flag : break
            if not flag : 
                answer.append(0)
                break
        else:
            answer.append(1)
                
                    
    return answer