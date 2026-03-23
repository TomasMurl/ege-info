def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

for x in range(1, 2031):
    s = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    s_6 = convert(s, 6)
    if s_6.count('0') == 202:
        print(x)
        break