def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

min_0 = 10000000000000
for x in range(1, 2031):
    s = 6 ** 2030 + 6 ** 100 - x
    s_6 = convert(s, 6)
    if s_6.count(0) < min_0:
        min_0 = s_6.count(0)
print(min_0)