def perevod(n, osn):
    res = []
    while n > 0:
        res.append(n % osn)
        n = n // osn
    return res[::-1]

s = 6 * 512 ** 180 + 7 * 64 ** 181 + 3 * 8 ** 184 + 5 * 8 ** 125 - 65
s_64 = perevod(s, 64)
print(s_64.count(0))