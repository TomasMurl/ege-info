for N in range(1, 10000000):
    N2 = bin(N)[2:]
    c0 = N2.count('0')
    c1 = N2.count('1')
    N2 = bin(c1)[2:] + bin(c0)[2:]
    R = int(N2, 2)
    if R == 156:
        print(N)
        break