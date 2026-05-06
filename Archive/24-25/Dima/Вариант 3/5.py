for N in range(1, 100):
    N_2 = bin(N)[2:]
    summa_1 = N_2.count("1")
    N_2 = N_2 + str(summa_1 % 2)
    summa_1 = N_2.count("1")
    N_2 = N_2 + str(summa_1 % 2)
    R = int(N_2, 2)
    if R > 75:
        print(R)