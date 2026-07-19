def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

min_R = 100000000
for N in range(1, 100):
    N3 = convert(N, 3)
    if N % 3 == 0:
        N3 = N3 + N3[-2:]
    else:
        # sc = 0
        # for i in N3:
        #     sc = sc + int(i)
        sc = sum([int(i) for i in N3]) # N3 = '12202' -> sc = 9
        N3 = N3 + convert(sc, 3)
    R = int(N3, 3)
    if R > 220 and R % 2 == 0:
        if R < min_R:
            min_R = R
print(min_R)