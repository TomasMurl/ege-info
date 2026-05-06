def perevod(n, osn):
    result = ""
    while n > 0:
        result = str(n % osn) + result
        n = n // osn
    return result

for x in range(1, 10000000):
    virazh = 3 ** 2000 + 3 ** 10 - x
    v_3 = perevod(virazh, 3)
    if v_3.count("2") == 2000:
        print(x)
        break