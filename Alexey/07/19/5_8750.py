def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n = n // b
    return r[::-1]

min_d = 1000000000
for N in range(1, 100000):
    N_3 = convert(N, 3)

    if N % 3 != 0:
        N_3 = '1' + N_3 + N_3[-3:]
    else:
        # sc = N_3.count('1') + N_3.count('2') * 2
        # generator -> list -> sum
        # generator -> sum
        sc = sum([int(i) for i in N_3])
        sc_else = convert(sc * 8, 3)
        N_3 = N_3 + sc_else
    R = int(N_3, 3)
    if abs(R - 1220) < min_d:
        min_d = abs(R - 1220)
        print(R, min_d)
