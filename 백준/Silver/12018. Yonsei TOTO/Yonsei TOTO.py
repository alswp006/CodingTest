#백준 12018번 yonsei TOTO

#idea
#정답 리스트를 만든 다음 과목 수만큼 반복문 돌리고 신청자 수가 과목 수강인원보다 적으면 정답 리스트에 append(1)
#아니라면 마일리지 리스트를 sort한 후 -과목수강인원 인덱스를 정답리스트에 append
#시간복잡도를 위해 과목 수강인원과 신청자 수가 같을 때는 min(list)

import sys

input = sys.stdin.readline

n,m = map(int,input().split())
answer_list=[]
answer=0

for _ in range(n):
    p,l=map(int,input().split())
    arr=list(map(int,input().split()))
    if p<l:
        answer_list.append(1)
    elif p==l:
        answer_list.append(min(arr))
    else:
        arr.sort()
        answer_list.append(arr[-l])
answer_list.sort()

target=0
for i in answer_list:
    target+=i
    if target>m:
        target-=i
        break
    answer+=1
    
print(answer)