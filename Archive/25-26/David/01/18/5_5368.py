for N in range(100, 0, -1):
    N_2 = bin(N)[2:]
    summa = N_2.count("1")
    if summa % 2 == 0:
        N_2 = "10" + N_2[2:] + "0"
    else:
        N_2 = "11" + N_2[2:] + "1"
    R = int(N_2, 2)
    if R < 35:
        print(N)
        break