def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

for x in range(1, 27001):
    s = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x
    s_27 = convert(s, 27)
    if s_27.count(0) == 6:
        print(x)
        break