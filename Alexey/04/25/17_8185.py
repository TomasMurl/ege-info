with open('17-433.txt') as f:
    m = list(map(int, f))

min_15 = min(i for i in m if str(i)[-2:] == '15' and 99 < abs(i) < 1000)

cnt = 0
min_pr = 10000000000000
for i in range(len(m) - 2):
    a, b, c = m[i], m[i+1], m[i+2]
    z = int(a >= 0) + int(b >= 0) + int(c >= 0)
    mi = min(a, b, c)
    ma = max(a, b, c)
    if (z == 0 or z == 3) and mi * ma > min_15 ** 2:
        cnt += 1
        min_pr = min(min_pr, mi * ma)
print(cnt, min_pr)
