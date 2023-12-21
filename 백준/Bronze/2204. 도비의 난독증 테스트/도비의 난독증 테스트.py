while True:
    num = int(input())
    if num == 0:
        break
    arr=dict()
    for i in range(num):
        s = input()
        arr[s.upper()] = s
    arr = sorted(arr.items())
    print(arr[0][1])