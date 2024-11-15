n = int(input())
s = int(input())
m = input()

l = len(m)
t = 0
s1 = "I"
answer = 0
for i in range(n):
    s1 += "OI"
s2 = s1[:len(s1)-2]

while l != t:
    m = m.replace(s1, s2)
    answer += (l - len(m)) // 2
    t = l
    l = len(m)
print(answer)