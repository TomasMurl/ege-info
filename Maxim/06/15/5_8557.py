def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

for N in range(1, 1000):
    N_3 = convert(N, 3)
    if N % 3 == 0:
        # N_3 = N_3 + N_3[-2] + N_3[-1]
        N_3 = N_3 + N_3[-2:]
    else:
        # "12012": 2 + 2 * 2 = 6
        sc = N_3.count('1') + N_3.count('2') * 2
        N_3 = N_3 + convert(sc * 3, 3)
    R = int(N_3, 3)
    if R % 2 != 0 and R > 208:
        print(R)