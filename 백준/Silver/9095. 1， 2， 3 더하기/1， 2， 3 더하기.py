for _ in range(int(input())):
    n = int(input())
    count = 0
    def cal(n):
        global count
        if n == 0:
            count += 1
            return -1
        if n<0: return -1
        for i in range(1,4):
            cal(n-i)
    cal(n)
    print(count)