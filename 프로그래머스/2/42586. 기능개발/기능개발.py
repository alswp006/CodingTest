def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)):
        arr.append((99 - progresses[i]) // speeds[i] + 1)
        
    prev = arr[0]
    temp = 1
    for i in range(1, len(arr)):
        if arr[i] <= prev:
            temp+=1
        else:
            answer.append(temp)
            temp = 1
            prev = arr[i]
    else:
        if temp != 0: answer.append(temp)   
    print(arr)
    return answer