for N in range(1, 100):
    N_2 = bin(N)[2:] # 0x
    summa = N_2.count("1")
    N_2 = N_2 + str(summa % 2)
    summa = N_2.count("1")
    N_2 = N_2 + str(summa % 2)
    R = int(N_2, 2)
    if R > 123:
        print(R)