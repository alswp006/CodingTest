def solution(park, routes):
    move = {"E" : (0,1), "W" : (0,-1), "S" : (1,0), "N" : (-1,0)}
    answer = [0,0]
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x, y = i, j
    
    for route in routes:
        a, b = map(str, route.split())
        b = int(b)
        temp_x, temp_y = x, y
        for i in range(b):
            nx, ny = temp_x + move[a][0], temp_y + move[a][1]
            if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]):
                break
            if park[nx][ny] == "X": break
            temp_x, temp_y = nx, ny
        else:
            x, y = temp_x, temp_y
        
    return [x, y]