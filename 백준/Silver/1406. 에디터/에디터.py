import sys

input=sys.stdin.readline

left=list(input().rstrip())
right=[]
for _ in range(int(input())):
    arr=input().split()
    if arr[0]=='L' and left:
        right.append(left.pop())
    elif arr[0]=='D' and right:
        left.append(right.pop())
    elif arr[0]=='B' and left:
        left.pop()
    elif arr[0]=='P':
        left.append(arr[1])

print("".join(left), end="")
print("".join(right[::-1]))