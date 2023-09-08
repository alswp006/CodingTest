#백준 1517번 버블 소트

import sys

input = sys.stdin.readline
result = 0 

def merge_sort(s, e):
    global result
    #더 이상 자를 수 없을 때 리턴
    if e-s<1 : return
    
    #반으로 자르는 연산
    m = s+(e-s)//2
    merge_sort(s,m)
    merge_sort(m+1,e)

    for i in range(s, e + 1):
        temp[i] = A[i]

    #투포인터 만들기
    k=s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:
        if temp[index1] > temp[index2]:
            A[k] = temp[index2]
            result += index2 - k
            k += 1
            index2 += 1
        else:
            A[k] = temp[index1]
            k += 1
            index1 += 1

    while index1 <= m:
        A[k] = temp[index1]
        k += 1
        index1 += 1 
    while index2 <= m:
        A[k] = temp[index2]
        k += 1
        index2 += 1 



N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
temp = [0] * (N+1)
merge_sort(1,N)
print(result)