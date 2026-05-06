def perevod(n, osn):
    res = ""
    while n > 0:
        res += str(n % osn)
        n = n // osn
    return res[::-1]

max_4 = 0
for x in range(10, 70001):
    n = 5 ** 2025 + 5 ** 400 - x
    n_5 = perevod(n, 5)
    if n_5.count("4") >= max_4:
        print(x)
        max_4 = n_5.count("4")