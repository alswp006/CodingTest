import sys

input = sys.stdin.readline

s=''
while True:
    answer_arr=[]
    s=input().rstrip()
    if s=='.':break
    for i in s:
        if i =='(' :
            answer_arr.append('(')
        elif i ==')':
            if len(answer_arr)==0:
                answer_arr.append(1)
                break
            if answer_arr[-1] == '(':
                answer_arr.pop()
            else:
                break
        elif i == '[':
            answer_arr.append('[')
        elif i == ']':
            if len(answer_arr)==0:
                answer_arr.append(1)
                break
            if answer_arr[-1] == '[':
                answer_arr.pop()
            else:
                break
    if len(answer_arr) == 0:
        print('yes')
    else:
        print('no')