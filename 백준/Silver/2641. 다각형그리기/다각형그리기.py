import sys

input = sys.stdin.readline
length = int(input())#표본수열의 길이를 받습니다.

stand = ' '.join(input().split())#기준이 될 표본수열을 받습니다.나중에 비교해줍니다.
copy = ''#반대방향으로 돌리는 경우를 아래 반복문으로 만들어줍니다.

for i in range(len(stand)-1,-1,-1):#회전방향과 상하좌우를 동시에 바꿔줍니다.
    if stand[i] == ' ':
        copy += ' '
    elif stand[i] == '1':
        copy += '3'
    elif stand[i] == '2':
        copy += '4'
    elif stand[i] == '3':
        copy += '1'
    elif stand[i] == '4':
        copy += '2'
        
stand = stand + ' ' + stand
copy = copy + ' ' + copy
#회전을 하는 경우이기 때문에 시작과 끝을 이어주는 느낌으로 표본수열을 늘려줍니다.
to_for = int(input())#본격적으로 비교할 모양수열들의 갯수
total = []#출력할 모양수열을 저장하는 리스트
for i in range(to_for):
    comp = ' '.join(input().split())#모양수열을 받습니다.
    if comp in stand or comp in copy:#모양수열을 두가지 회전방향으로 검사합니다.
        total.append(comp)#맞다면 total리스트에 추가합니다.
print(len(total))#원소의 갯수 출력
for ans in total:
    print(ans)#원소 출력 형식에 맞게 줄바꿔서 출력