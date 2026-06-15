def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

for x in range(1, 2301):
    s = 7 ** 350 + 7 ** 150 - x
    s_7 = convert(s, 7)
    if s_7.count(0) == 200:
        print(x)