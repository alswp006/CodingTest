import sys
def check_knight():
    for i in range(len(arr)):
        alp = abs(ord(arr[i - 1][0]) - ord(arr[i][0]))
        num = abs(int(arr[i - 1][1]) - int(arr[i][1]))

        if not ((alp == 2 and num == 1) or (alp == 1 and num == 2)) :
            return False
    return True


arr = [sys.stdin.readline().rstrip() for i in range(36)]

print("Invalid" if len(set(arr)) != 36 or check_knight() == False else "Valid")