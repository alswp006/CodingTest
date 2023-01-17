def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append(format(arr1[i]|arr2[i],'b').zfill(n))
        answer[i]=answer[i].replace("1","#")
        answer[i]=answer[i].replace("0"," ")
    return answer