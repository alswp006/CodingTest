def fib(n):
    global count
    if n == 1 or n == 2:
        return 1
    count += 1
    return fib(n - 1) + fib(n - 2)


def fib_DP(n, count):
    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 1
    for i in range(3, n):
        count += 1
        arr[i] = arr[i - 1] + arr[i - 2]
    return count


n = int(input())

count = 1
fib(n)
print(count, end=' ')

count = 1
print(fib_DP(n, count))