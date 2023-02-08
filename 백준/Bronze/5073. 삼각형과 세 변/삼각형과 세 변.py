answer=[]
while True:
    arr=list(map(int,input().split()))
    if arr==[0,0,0]:break
    arr.sort()
    if arr[0]+arr[1]<=arr[2]:answer.append("Invalid")
    elif arr[0]==arr[1]==arr[2]:answer.append("Equilateral")
    elif arr[0]==arr[1]or arr[1]==arr[2] or arr[0]==arr[2]:answer.append("Isosceles")
    else : answer.append("Scalene")
for i in answer:print(i)