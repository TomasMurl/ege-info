for N in range(1, 100):
    N_2 = bin(N)[2:]
    s = N_2.count('1')
    if s % 2 == 0:
        N_2_new = '10' + N_2[2:] + '0'
    else:
        N_2_new = '11' + N_2[2:] + '1'

    R = int(N_2_new, 2)
    if R > 40:
        print(N)
        break
