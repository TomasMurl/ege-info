for N in range(1, 1000):
    N_2 = bin(N)[2:]
    if N % 2 == 0:
        N_2 = N_2 + "10"
    else:
        N_2 = "1" + N_2 + "01"
    R = int(N_2, 2)
    if R > 516:
        print(N)
        break