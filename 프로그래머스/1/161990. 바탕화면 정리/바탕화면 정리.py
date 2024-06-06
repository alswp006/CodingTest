def solution(wallpaper):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    
    for i in range(len(wallpaper)):
        flag = True
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                min_x = i
                flag = False
                break
        if not flag : break
        
    for i in range(len(wallpaper) - 1, -1, -1):
        flag = True
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                max_x = i
                flag = False
                break
        if not flag : break
        
    for i in range(len(wallpaper[0])):
        flag = True
        for j in range(len(wallpaper)):
            if wallpaper[j][i] == "#":
                min_y = i
                flag = False
                break
        if not flag : break

    for i in range(len(wallpaper[0]) - 1, -1, -1):
        flag = True
        for j in range(len(wallpaper)):
            if wallpaper[j][i] == "#":
                max_y = i
                flag = False
                break
        if not flag : break
        
    return [min_x, min_y, max_x + 1, max_y + 1]