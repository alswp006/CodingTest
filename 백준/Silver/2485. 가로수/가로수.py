import sys
from math import gcd

input = sys.stdin.readline

n = int(input())
temp1 = int(input())
temp2 = int(input())
arr = [temp2 - temp1]
g = temp2 - temp1
temp1 = temp2
answer = 0

for _ in range(n - 2):
    temp2 = int(input())
    arr.append(temp2 - temp1)
    g = gcd(g, temp2 - temp1)
    temp1 = temp2

for i in arr:
    answer += i // g - 1

print(answer)