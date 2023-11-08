import sys

sys.setrecursionlimit(10**4)

def quick_sort(arr, start, end):
    if start < end:
        q = partition(arr, start, end)
        quick_sort(arr, start, q - 1)
        quick_sort(arr, q + 1, end)


def partition(arr, start, end):
    global y, count

    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            count += 1
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            if y==count :
                print(min(arr[i], arr[j]), max(arr[i], arr[j]))
                exit()
    if i + 1 != end:
        count += 1
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        if y == count:
            print(min(arr[i+1], arr[end]), max(arr[i+1], arr[end]))
            exit()

    return i + 1


count = 0
x, y = map(int,input().split())
arr = list(map(int, input().split()))
quick_sort(arr, 0, len(arr) - 1)
print(-1)