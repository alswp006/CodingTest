n = int(input())
end, total, count = 0, 0, 0

for start in range(n):
    while total < n and end < n:
        total += end + 1
        end += 1
    if total == n: count += 1
    total -= start + 1
print(count)