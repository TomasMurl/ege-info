def perevod(n, osn):
    result = []
    while n > 0:
        result.append(n % osn)
        n = n // osn
    return result[::-1]

# 10 = 0123456789
# 16 = 0123456789ABCDEF

for x in range(7050, 0, -1):
    v = 5 ** 100 - x
    v_5 = perevod(v, 5)
    if v_5.count(0) == 3:
        print(x)
        break