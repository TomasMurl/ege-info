def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

for x in range(1, 2031):
    s = 7 ** 91 + 7 ** 160 - x
    s_7 = convert(s, 7)
    if s_7.count('0') == 70:
        print(x)