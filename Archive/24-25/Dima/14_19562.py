def perevod(n, osn):
    res = []
    while n > 0:
        res.append(n % osn)
        n = n // osn
    return res[::-1]

s = 16807 ** 35 + 2401 ** 2 * 343 ** 9 - 49 ** 52 + 7 ** 3 - 2005
s_49 = perevod(s, 49)
c = 0
for x in s_49: # [1, 2, 4, 3, 2 ,4, 5]
    if x > 9:
        c += 1
print(c)