def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

for x in range(1, 3001):
    s = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    s_11 = convert(s, 11)
    if s_11.count(0) == 60:
        print(x)