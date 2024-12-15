DIV = 1000000007

def power(a, m):
    if m == 0:
        return 1
    temp = power(a, m // 2) % DIV
    if m % 2 == 1:
        return temp * temp % DIV * a % DIV
    return temp * temp % DIV

def solve(n, k):
    if k == 0 or n == k:
        print(1)
        return
    if k == 1 or n - k == 1:
        print(n)
        return

    A = 1
    B = 1

    for i in range(n, n - k, -1):
        A = (A * i) % DIV
    
    for i in range(1, k + 1):
        B = (B * i) % DIV

    ans = (A * power(B, DIV - 2)) % DIV
    print(ans)

if __name__ == "__main__":
    n, k = map(int, input().split())
    solve(n, k)