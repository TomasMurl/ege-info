def perevod(n, osn):
    res = []
    while n > 0:
        res.append(n % osn)
        n = n // osn
    return res[::-1]

s = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005
s_25 = perevod(s, 25)
print(s_25.count(0))