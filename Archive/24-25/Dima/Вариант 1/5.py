for N in range(1, 13):
    N_2 = bin(N)[2:]
    if N % 2 == 0:
        N_2 = "10" + N_2
    if N % 2 == 1:
        N_2 = "1" + N_2 + "01"
    R = int(N_2, 2)
    print(N, R)