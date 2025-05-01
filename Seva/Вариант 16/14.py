def perevod(n, osn):
    res = []
    while n > 0:
        res.append(n % osn)
        n = n // osn
    return res[::-1]

for x in range(1, 7051):
    result = perevod(5 ** 100 - x, 5)
    if result.count(0) == 3:
        print(x, result)
    