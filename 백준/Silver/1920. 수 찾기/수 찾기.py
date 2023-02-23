import sys
import sys
input = sys.stdin.readline
n=input()
arr=set(input().split())
m=input()
arr2=['1' if i in arr else '0' for i in input().split()]

for i in arr2:print(i)