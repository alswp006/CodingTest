import sys

def camelCase(s):
    print(s)
    for i in s:
        if ord(i) < 97:
            print("_", end='')
            print(chr(ord(i) + 32), end='')
        else:
            print(i, end='')
    print()
    for i in range(len(s)):
        if i == 0:
            print(chr(ord(s[i]) - 32), end='')
        else:
            print(s[i], end='')

def snakeCase(s):
    arr = list(s.split("_"))
    for i in range(len(arr)):
        if i == 0:
            print(arr[i], end='')
        else:
            print(arr[i].capitalize(), end='')
    print()
    print(s)
    for i in arr:
        print(i.capitalize(), end='')

def pascalCase(s):
    for i in range(len(s)):
        if i == 0:
            print(chr(ord(s[i]) + 32), end='')
        else:
            print(s[i], end='')
    print()
    for i in range(len(s)):
        if i != 0:
            if ord(s[i]) < 97:
                print("_", end='')
                print(chr(ord(s[i]) + 32), end='')
            else:
                print(s[i], end='')
        else:
            if ord(s[i]) < 97:
                print(chr(ord(s[i]) + 32), end='')
            else:
                print(s[i], end='')
    print()
    print(s)

n, s = map(str, sys.stdin.readline().rstrip().split())
n = int(n)

if n == 1:
    camelCase(s)
elif n == 2:
    snakeCase(s)
elif n == 3:
    pascalCase(s)