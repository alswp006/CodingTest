n = int(input())
p, w_t = [0, 0], [0, 0]
p_t = 0

for i in range(n):
    team, t_s = map(str, input().split())
    time = int(t_s[:2]) * 60 + int(t_s[3:])
    w_t[p[0] < p[1]] += time - p_t if p[0] != p[1] else 0
    p[int(team) - 1] += 1
    p_t = time
w_t[p[0] < p[1]] += 48 * 60 - p_t if p[0] != p[1] else 0

print(f'{w_t[0] // 60:02}:{w_t[0] % 60:02}')
print(f'{w_t[1] // 60:02}:{w_t[1] % 60:02}')
