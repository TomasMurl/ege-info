def perevod(n, o):
    r = []
    while n > 0:
        r.append(n % o)
        n = n // o
    return r[::-1]

for x in reversed(range(1, 2031)):
    v = 7 ** 170 + 7 ** 100 - x
    v_7 = perevod(v, 7)
    if v_7.count(0) == 71:
        print(x)
        break