def solution(lottos, win_nums):
    answer = []
    num=0
    n=lottos.count(0)
    for i in range(n):lottos.remove(0)
    for i in range(len(lottos)):num+=win_nums.count(lottos[i])
    if num<2: 
        answer.append(6)
        answer.insert(0,answer[0]-n)
    elif num==2: 
        answer.append(5)
        answer.insert(0,answer[0]-n)
    elif num==3: 
        answer.append(4)
        answer.insert(0,answer[0]-n)
    elif num==4: 
        answer.append(3)
        answer.insert(0,answer[0]-n)
    elif num==5: 
        answer.append(2)
        answer.insert(0,answer[0]-n)
    elif num==6: 
        answer.append(1)
        answer.insert(0,answer[0]-n)
    if answer[0]<1 : answer[0]=1
    return answer