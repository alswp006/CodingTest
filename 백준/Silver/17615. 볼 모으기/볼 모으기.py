import sys

input = sys.stdin.readline

n = int(input())
s = input().rstrip()

def move(ball1):
    temp_answer = 0

    for i in s.rstrip(ball1):
        if i == ball1:
            temp_answer += 1

    temp = 0
    for i in reversed(s.lstrip(ball1)):
        if temp > temp_answer:
            break
        if i == ball1:
            temp += 1
    else:
        temp_answer = temp

    return temp_answer


answer = min(move("R"), move("B"))
print(answer)
