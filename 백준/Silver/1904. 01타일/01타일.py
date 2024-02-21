# 피사노 주기 구하기
# def pisano_period(m):
#     previous, current = 0, 1
#     for i in range(0, m * m):
#         previous, current = current, (previous + current) % m
#
#         # 피사노 주기는 항상 0과 1로 시작합니다.
#         if (previous == 0 and current == 1):
#             return i + 1
# m = 15746일 때 피사노 주기 47244
a, b = 1,2

n = int(input())
for i in range(n % 47244 - 2):
    a, b = b, (a+b) % 15746

print(b if n != 1 else a)