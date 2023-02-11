import sys

n= input()
num= set(input().split())
m= input()
num2=[i for i in input().split()]
for i in num2:
    print('1' if i in num else '0' )