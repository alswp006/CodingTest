import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
nums = set(int(''.join(map(str, perm))) for perm in permutations(range(1, 10), 3))

for _ in range(n):
    num, s, b = map(int, input().split())
    invalid_nums = set()

    for check in nums:
        cnt_s, cnt_b = 0, 0

        check_str = str(check)
        num_str = str(num)

        for i in range(3):
            if num_str[i] == check_str[i]:
                cnt_s += 1
            elif num_str[i] in check_str:
                cnt_b += 1

        if s != cnt_s or b != cnt_b:
            invalid_nums.add(check) 

    nums -= invalid_nums

print(len(nums))
