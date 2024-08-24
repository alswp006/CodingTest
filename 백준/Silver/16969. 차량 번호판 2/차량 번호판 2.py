s = input()
temp = s[0]
d = {'c':26, 'd':10}
answer = d[temp]
for i in s[1:]:
    answer *= d[i]-1 if i == temp else d[i]
    answer %= 1000000009
    temp = i
print(answer)