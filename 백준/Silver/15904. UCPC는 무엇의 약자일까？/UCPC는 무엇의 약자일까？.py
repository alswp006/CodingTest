n = input()
s = ["U", "C", "P", "C"]
idx = 0

for i in n:
    if i == s[idx]:
        idx += 1
    if idx  == 4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")