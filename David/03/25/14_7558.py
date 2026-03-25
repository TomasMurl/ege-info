def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

m = 0
for x in range(1, 2030):
    s = 6 ** 2030 + 6 ** 100 - x
    s_6 = convert(s, 6)
    if s_6.count(0) > m:
        m = s_6.count(0)
print(m)