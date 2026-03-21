def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

for x in range(1, 2301):
    s = 7 ** 350 + 7 ** 150 - x
    s_4 = convert(s, 7)
    if s_4.count('0') == 200:
        print(x)