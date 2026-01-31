def perevod(n, osn):
    result = ''
    while n > 0:
        result = str(n % osn) + result
        n = n // osn
    return result

for N in range(1, 100):
    N_3 = perevod(N, 3)
    if N % 3 == 0:
        N_3 = N_3 + N_3[-2:]
    else:
        ost = N % 3 * 3
        ost_3 = perevod(ost, 3)
        N_3 = N_3 + ost_3
    R = int(N_3, 3)
    if R <= 150:
        print(N)
