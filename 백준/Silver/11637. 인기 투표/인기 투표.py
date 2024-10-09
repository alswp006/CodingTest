import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a = [int(input()) for _ in range(int(input()))]
    m = max(a)
    print('no winner' if a.count(m) > 1 else f"{['minority', 'majority'][m > sum(a) // 2]} winner {a.index(m) + 1}")
