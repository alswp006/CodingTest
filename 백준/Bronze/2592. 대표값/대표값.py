import sys

input = sys.stdin.readline

arr = [0] * 100
answer = 0
m = 0
avg = 0

for i in range(10):
    n = int(input())
    arr[n//10] += 1
    avg+=n
    
for i in range(len(arr)):
    if m < arr[i]:
        answer = i * 10
        m = arr[i]
  
print(avg//10)
print(answer)