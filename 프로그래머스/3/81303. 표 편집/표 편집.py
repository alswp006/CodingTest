table = dict()
stack = []
answer = []


def delete_data(pointer):
    prev, next = table[pointer]
    stack.append([prev, pointer, next])
    if next == None:
        pointer = table[pointer][0]
    else:
        pointer = table[pointer][1]
    if prev == None:
        table[next][0] = None
    elif next == None:
        table[prev][1] = None
    else:
        table[prev][1] = next
        table[next][0] = prev
    return pointer


def restore_data():
    prev, now, next = stack.pop()
    answer[now] = 'O'
    if prev == None:
        table[next][0] = now
    elif next == None:
        table[prev][1] = now
    else:
        table[next][0] = now
        table[prev][1] = now


def move(c1, c2, pointer):
    if c1 == 'D':
        for _ in range(c2):
            pointer = table[pointer][1]
    else:
        for _ in range(c2):
            pointer = table[pointer][0]
    return pointer


def solution(n, k, cmd):
    pointer = k
    for i in range(n):
        table[i] = [i-1, i+1]
    table[0][0] = None
    table[n - 1][1] = None
    for i in range(n):
        answer.append("O")

    for c in cmd:
        if c == "C":
            answer[pointer] = 'X'
            pointer = delete_data(pointer)
        elif c == "Z":
            restore_data()
        else:
            c1, c2 = c.split(' ')
            pointer = move(c1, int(c2), pointer)

    return ''.join(answer)