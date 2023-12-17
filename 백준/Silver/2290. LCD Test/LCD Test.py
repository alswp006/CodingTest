s, n = map(str, input().split())
s = int(s)

dash = '-'
bar = '|'

segments = {
    '0': ['a', 'b', 'c', 'e', 'f', 'd'],
    '1': ['b', 'c'],
    '2': ['a', 'b', 'g', 'e', 'd'],
    '3': ['a', 'b', 'g', 'c', 'd'],
    '4': ['f', 'g', 'b', 'c'],
    '5': ['a', 'f', 'g', 'c', 'd'],
    '6': ['a', 'f', 'g', 'e', 'c', 'd'],
    '7': ['a', 'b', 'c'],
    '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    '9': ['a', 'b', 'c', 'd', 'f', 'g']
}

def draw_segment(segment, lcd):
    if segment == 'a':
        for i in range(1, s+1):
            lcd[0][i] = dash
    elif segment == 'b':
        for i in range(1, s+1):
            lcd[i][s+1] = bar
    elif segment == 'c':
        for i in range(s+2, 2*s+2):
            lcd[i][s+1] = bar
    elif segment == 'd':
        for i in range(1, s+1):
            lcd[2*s+2][i] = dash
    elif segment == 'e':
        for i in range(s+2, 2*s+2):
            lcd[i][0] = bar
    elif segment == 'f':
        for i in range(1, s+1):
            lcd[i][0] = bar
    elif segment == 'g':
        for i in range(1, s+1):
            lcd[s+1][i] = dash

def draw_number(number):
    lcd = [[' '] * (s + 2) for _ in range(2 * s + 3)]
    for segment in segments[number]:
        draw_segment(segment, lcd)
    return lcd


answer = [draw_number(i) for i in n]

for line in zip(*answer):
    for r in line:
        print(''.join(r), end=' ')
    print()

