s1 = input()
s2 = list(input())
num = len(s2)
while len(s1) < num:
    temp = s2.pop()
    if temp == "B":
        s2.reverse()
    num -= 1
print(int(s1 == ''.join(s2)))