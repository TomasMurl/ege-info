for N in range(1, 1000):
    N2 = bin(N)[2:]
    if N % 3 == 0:
        N2 = N2 + N2[-3:]
    else:
        N2 = N2 + bin(N % 3 * 3)[2:]
    R = int(N2, 2)
    if R >= 200:
        print(N, R)
        break