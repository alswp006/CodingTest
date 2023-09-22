n=int(input())
answer=0

for i in range((n+1)//3,(n+1)//2):
    small_side = n - (i*2)
    answer+=(i-small_side)//2+1
print(answer)