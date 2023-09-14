import sys

input = sys.stdin.readline

length = int(input())
stand = list(map(str,input().split()))
reverse = []

for i in range(length-1,-1,-1):#회전방향과 상하좌우를 동시에 바꿔줍니다.
    if stand[i] == '1':
        reverse.append('3')
    elif stand[i] == '2':
        reverse.append('4')
    elif stand[i] == '3':
        reverse.append('1')
    elif stand[i] == '4':
        reverse.append('2')

#표본 수열 두 번 반복하기
temp=stand+stand
stand = ' '.join(temp)
temp=reverse+reverse
reverse = ' '.join(temp)

#모양 수열 비교
answer = []
for _ in range(int(input())):
    comp = ' '.join(input().split())
    if comp in stand or comp in reverse:
        answer.append(comp)

#정답 출력
print(len(answer))
for ans in answer:
    print(ans)