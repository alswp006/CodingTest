import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a,b=map(int,input().split())
    answer=a*b
    while b:
        a,b=b,a%b
    print(answer//a)