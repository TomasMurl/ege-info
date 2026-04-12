def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

s = 343 ** 1515 - 6 * 49 ** 1520 + 5 * 49 ** 1510 - 3 * 7 ** 1530 - 1550
s_7 = convert(s, 7)
print(s_7.count(0))