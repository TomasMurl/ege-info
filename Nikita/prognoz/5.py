def perevod(n, osn):
    res = ''
    # res = []
    while n > 0:
        # res.append(n % osn)
        res += str(n % osn)
        n = n // osn
    return res[::-1]

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