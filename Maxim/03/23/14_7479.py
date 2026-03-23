def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

for x in range(5000, 20000):
    s = 7 ** 100 - x
    s_7 = convert(s, 7)
    if s_7.count('0') == 5:
        print(x)
        break