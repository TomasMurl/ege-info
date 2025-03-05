for N in range(1, 100):
    N_2 = bin(N)[2:] # "1010101"
    a = N_2.count("1") % 2
    N_2 = N_2 + str(a)
    b = N_2.count("1") % 2
    N_2 = N_2 + str(b)
    R = int(N_2, 2)
    if R > 123:
        print(R)