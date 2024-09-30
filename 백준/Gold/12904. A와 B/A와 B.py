s1 = input()
s2 = list(input())
while len(s1) < len(s2):
    temp = s2.pop()
    if temp == "B":
        s2 = s2[::-1]
print(int(s1 == ''.join(s2)))