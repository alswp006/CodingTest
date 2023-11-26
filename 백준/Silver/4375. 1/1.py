while True:
    try:
        n = int(input())
    except Exception:
        break
    num = 1

    while num % n != 0:
        num = num * 10 + 1
    print(len(str(num)))