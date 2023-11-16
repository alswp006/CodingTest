n = int(input())
arr = list(map(int,input().split()))

d = [0 for i in range(n)]

for i in range(n):
    d[i] = max(d[i-1]+arr[i], arr[i])

print(max(d))