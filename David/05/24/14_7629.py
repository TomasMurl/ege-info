def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

for x in range(1, 2031):
    s = 7 ** 170 + 7 ** 100 - x
    s_7 = convert(s, 7)
    if s_7.count(0) == 71:
        print(x)