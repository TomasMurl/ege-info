for N in range(1, 100):
    N_2 = bin(N)[2:]

    s = N_2.count('1') % 2
    N_2 = N_2 + str(s)

    s = N_2.count('1') % 2
    N_2 = N_2 + str(s)

    R = int(N_2, 2)
    if R > 85:
        print(N)
        break
