def perevod(n, osn):
    res = ''
    while n > 0:
        res = str(n % osn) + res
        n = n // osn
    return res

for N in range(1, 100):
    N_3 = perevod(N, 3)
    if N % 3 == 0:
        N_3 = N_3 + N_3[-2:]
    else:
        N_3 = N_3 + perevod(N % 3 * 5, 3)
    R = int(N_3, 3)
    if R >= 290:
        print(N)
        break