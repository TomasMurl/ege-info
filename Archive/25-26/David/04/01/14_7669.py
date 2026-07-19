def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

m = 0
for x in range(1, 2001):
    s = 9 ** 250 + 9 ** 150 - x
    s_9 = convert(s, 9)
    if s_9.count('1') > m:
        m = s_9.count('1')
    if s_9.count('1') == m:
        print(x, s_9.count('1'))