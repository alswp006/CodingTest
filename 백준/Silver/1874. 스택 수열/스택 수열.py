import sys

input = sys.stdin.readline

cnt = int(input())
stack = []
answer = []
num = 1

for _ in range(cnt):
    n = int(input())
    if answer and answer[0] == "NO":
        continue
    if n == num:
        answer.append("+")
        answer.append("-")
        num += 1
        continue
    if not stack:
        stack.append(num)
        answer.append("+")
        num += 1
    while stack[-1] != n:
        if num > cnt:
            break
        stack.append(num)
        answer.append("+")
        num += 1
    if stack[-1] == n:
        stack.pop()
        answer.append("-")
    else:
        answer = ["NO"]

for i in answer:
    print(i)
