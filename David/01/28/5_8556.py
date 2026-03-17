for N in range(1, 100):
    N_2 = bin(N)[2:]
    if N % 3 == 0:
        N_2 = N_2 + N_2[-3:]
    else:
        ost = N % 3 * 3
        ost_2 = bin(ost)[2:]
        N_2 = N_2 + ost_2
    R = int(N_2, 2)
    if R >= 200:
        print(N)
        break