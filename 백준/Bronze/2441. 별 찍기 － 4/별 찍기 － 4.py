n=int(input())

arr=['*' for i in range(n)]

for i in range(n):
       print(''.join(arr))
       arr[i]=' '