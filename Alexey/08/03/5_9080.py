for N in range(1, 1000):
    N_2 = bin(N)[2:]
    if str(N_2).count("1") % 2 == 0:
        N_2 = "10" + str(N_2)[2:] + "0"
    else:
        N_2 = "11" + str(N_2)[2:] + "1"
    R = int(N_2,2)
    if R >= 16:
        print(N)
        break