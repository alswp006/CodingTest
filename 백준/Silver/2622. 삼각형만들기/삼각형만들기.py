n=int(input())
answer=0
largestSide=0

if n%2==0:
    largestSide = n // 2 - 1
else:
    largestSide=n // 2
for i in range(largestSide,n//3,-1):
    m=0
    big_side = i-m
    small_side = n - i - big_side
    while big_side>=small_side:
        answer+=1
        m+=1
        big_side=i-m
        small_side=n-i-big_side
if n%3==0:
    answer+=1
print(answer)