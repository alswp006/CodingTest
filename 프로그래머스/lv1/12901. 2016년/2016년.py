def solution(a, b):
    num=0
    week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    mon=[0,31,29,31,30,31,30,31,31,30,31,30]
    for i in range(0,a) : num+=mon[i]
    return week[(num+b)%7]