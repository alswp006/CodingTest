while True:
    try:
        n = int(input())
    except Exception:
        break
    i = 1
    num = 1

    while num % n != 0:
        num = num * 10 + 1
        i += 1
    print(i)