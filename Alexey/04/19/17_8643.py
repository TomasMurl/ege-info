with open('17-444.txt') as f:
    m = list(map(int, f))

max_30 = max(x for x in m if str(x)[-2:] == '30')

cnt = 0
max_sum = -300000
for i in range(len(m) - 2):
    a, b, c = m[i], m[i + 1], m[i + 2]
    if all(len(str(abs(x))) != 4 for x in [a, b, c]) \
            and a + b + c > max_30:
        cnt += 1
        max_sum = max(max_sum, a + b + c)
print(cnt, max_sum)
