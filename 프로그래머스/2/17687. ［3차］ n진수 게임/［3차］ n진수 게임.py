def solution(n, t, m, p):
    num = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    num = num[:n + 1]
    arr = ["0"]
    
    i = 1
    while len(arr) <= m * t:
        temp_i = i
        temp = []
        while temp_i > 0:
            temp.append(temp_i%n)
            temp_i//=n
        for j in temp[::-1]:
            arr.append(num[j])
        i += 1
        
    arr = arr[:t*m]
    
    return ''.join([arr[i] for i in range(p - 1,len(arr), m)])