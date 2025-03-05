for N in range(1, 100):
    N_s = N
    N_3 = ''
    while N > 0:
        N_3 = str(N % 3) + N_3
        N = N // 3