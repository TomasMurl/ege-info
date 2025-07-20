def perevod(n, osn):
    otv = ''
    while n > 0:
        otv = str(n % osn) + otv
        n = n // osn
    return otv

max_4 = -1000000000
for x in range(10, 70001):
    v = 5 ** 2025 + 5 ** 400 - x
    v_5 = perevod(v, 5)
    if v_5.count('4') >= max_4:
        max_4 = v_5.count('4')
        print(max_4, x)