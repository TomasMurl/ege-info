def perevod(n, osn):
    res = []
    while n > 0:
        res.append(n % osn)
        n = n // osn
    return res[::-1]

for x in range(2300, 0, -1):
    s = 7 ** 350 + 7 ** 150 - x
    s_7 = perevod(s, 7)
    if s_7.count(0) == 200:
        print(x)
        break