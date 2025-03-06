def perevod(n, osn):
    otv = ''
    while n > 0:
        otv = str(n % osn) + otv
        n = n // osn
    return otv

for N in range(1, 10000):
    N_3 = perevod(N, 3)
    if N % 2 == 0:
        N_3 = "1" + N_3 + "00"
    else:
        summa_cifr = 0
        for i in N_3:
            summa_cifr += int(i)
        N_3 = N_3 + perevod(summa_cifr, 3)
    R = int(N_3, 3)
    if R > 168:
        print(N, R)
        break