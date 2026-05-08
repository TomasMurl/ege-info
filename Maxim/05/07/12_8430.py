for N in range(1, 70000):
    N_2 = bin(N)[2:]
    N_2 = N_2.replace('0', '2')
    N_2 = N_2.replace('1', '0')
    N_2 = N_2.replace('2', '1')
    if int(N_2, 2) == 415:
        print(N)