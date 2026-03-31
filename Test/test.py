def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

for x in range(2030, 0, -1):
    s = 7 ** 170 + 7 ** 100 - x
    s_7 = convert(s, 7)
    if s_7.count('0') == 71:
        print(x)
        break