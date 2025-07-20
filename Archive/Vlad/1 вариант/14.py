def perevod2(ch, osn):
    r = []
    while ch > 0:
        r.append(ch % osn)
        ch = ch // osn
    return r[::-1]

for x in range(1, 3 ** 2000):
    v = 3 ** 2000 + 3 ** 10 - x
    v_3 = perevod2(v, 3)
    if v_3.count(2) == 2000:
        print(x)
        break