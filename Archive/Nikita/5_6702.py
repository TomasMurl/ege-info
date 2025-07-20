for N in range(1, 100):
    N_2 = bin(N)[2:] # 0x0101010
    if N % 3 == 0:
        N_new = N_2 + N_2[-3:]
    else:
        ostatok = N % 3 * 3
        N_new = N_2 + bin(ostatok)[2:]
    R = int(N_new, 2)
    if R < 170:
        print(N, R)