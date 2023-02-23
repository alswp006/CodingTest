import math
k=int(input())
arr=[0,1,2,3,4,5,6,7,8,9]
answer=(math.factorial(len(arr)+k-1)//math.factorial(len(arr)-1))//(math.factorial(k))
print(answer%10007)