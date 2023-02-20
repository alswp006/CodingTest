def solution(num,n):
    arr=[0]
    for i in num:
        temp=[]
        for j in arr:
            temp.append(i+j)
            temp.append(j-i)
        arr=temp
    return arr.count(n)