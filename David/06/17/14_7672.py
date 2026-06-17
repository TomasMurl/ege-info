def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

max_4 = 0
for x in range(10, 70001):
    s = 5 ** 2025 + 5 ** 400 - x
    s_5 = convert(s, 5)
    if s_5.count(4) >= max_4:
        max_4 = s_5.count(4)
        print(x)