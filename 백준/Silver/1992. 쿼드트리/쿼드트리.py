import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip())) for i in range(n)]
answer = []


def d(n, temp_arr):
    s = sum([sum(i) for i in temp_arr])
    if n * n == s or s == 0:
        answer.append(str(temp_arr[0][0]))
        return

    temp_arr1 = []
    temp_arr2 = []
    temp_arr3 = []
    temp_arr4 = []

    for i in range(len(temp_arr)):
        if i < len(temp_arr) // 2:
            temp_arr1.append(temp_arr[i][:len(temp_arr) // 2])
            temp_arr2.append(temp_arr[i][len(temp_arr) // 2:])
            continue
        temp_arr3.append(temp_arr[i][:len(temp_arr) // 2])
        temp_arr4.append(temp_arr[i][len(temp_arr) // 2:])
    answer.append("(")
    d(n // 2, temp_arr1)
    d(n // 2, temp_arr2)
    d(n // 2, temp_arr3)
    d(n // 2, temp_arr4)
    answer.append(")")
    return

d(n, arr)
print(''.join(answer))