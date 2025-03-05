def perevod(c, n):
    r = []
    while c != 0:
        r.append(c % n)
        c = c // n
    return r[::-1]

alf = "01234567"

for x in alf:
    res = int("57A"+x+"9",16) * int("54"+x, 8)
    res_12 = perevod(res, 12)
    if sum(res_12) == 40:
        print(x, res)
