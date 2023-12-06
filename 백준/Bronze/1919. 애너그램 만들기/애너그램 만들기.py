a = [0] * 26
b = [0] * 26
ans = 0

for i in input():
    a[ord(i) - 97] += 1
for i in input():
    b[ord(i) - 97] += 1
for i in range(len(a)):
    ans += abs(a[i] - b[i])
print(ans)