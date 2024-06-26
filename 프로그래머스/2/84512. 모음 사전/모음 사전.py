def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    arr = [5**i for i in range(len(alphabet))]
    
    for i in range(len(word)-1, -1, -1):
        idx = alphabet.index(word[i])
        for j in range(5-i):
            answer += arr[j]*idx
        answer+=1
    return answer