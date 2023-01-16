def solution(answers):
    answer = []
    arr=[0,0,0]
    n1=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    n2=[2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    n3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if n1[i%len(n1)]==answers[i] : arr[0]+=1
        if n2[i%len(n2)]==answers[i] : arr[1]+=1
        if n3[i%len(n3)]==answers[i] : arr[2]+=1
    for i in range(0,3):
        if arr[i]==max(arr) : 
            answer.append(i+1)
    return answer