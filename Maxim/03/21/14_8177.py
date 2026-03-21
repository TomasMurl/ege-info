def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

max_0 = 0
for x in range(1, 3001):
    s = 4 ** 210 + 4 ** 110 - x
    s_4 = convert(s, 4)
    if s_4.count('0') > max_0:
        max_0 = s_4.count('0')

for x in range(1, 3001):
    s = 4 ** 210 + 4 ** 110 - x
    s_4 = convert(s, 4)
    if s_4.count('0') == max_0:
        print(x)
        break