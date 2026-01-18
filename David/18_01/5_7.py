for N in range(1, 100):
    # 1
    N_2 = bin(N)[2:]
    # 2
    # а)
    summa = N_2.count("1") # count возращает int
    ostatok = summa % 2 # int
    N_2 = N_2 + str(ostatok) # 1010 + 1 = 10101
    # б)
    summa = N_2.count("1")
    ostatok = summa % 2
    N_2 = N_2 + str(ostatok)
    R = int(N_2, 2)
    if R > 125:
        print(N)
        break
