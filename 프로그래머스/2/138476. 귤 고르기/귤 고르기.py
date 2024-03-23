def solution(k, tangerine):
    answer = 0
    arr = [0] * 10000001
    
    for i in tangerine:
        arr[i] += 1
    
    arr.sort(reverse = True)
    
    for i in range(len(arr)):
        if k - arr[i] <= 0:
            answer = i + 1
            break
        k -= arr[i]
    
    return answer