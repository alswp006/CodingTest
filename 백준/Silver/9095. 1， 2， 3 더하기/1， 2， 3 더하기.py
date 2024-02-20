import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    count = 0
    stack = [(n, 0)]  # 스택에 (숫자, 횟수) 형태로 저장합니다.

    while stack:
        num, cnt = stack.pop()

        if num == 0:
            count += 1
            continue

        for i in range(1, 4):
            if num - i >= 0:
                stack.append((num - i, cnt + 1))

    print(count)
