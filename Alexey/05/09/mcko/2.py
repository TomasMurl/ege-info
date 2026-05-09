for N in range(1, 100):
    N_2 = bin(N)[2:]
    if N % 2 == 0:
        N_2 += '10'
    else:
        N_2 = '1' + N_2 + '00'
    R = int(N_2, 2)
    if R > 107:
        print(N)
        break