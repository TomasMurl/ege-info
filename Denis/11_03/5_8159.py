for N in range(1, 1000):
    N2 = bin(N)[2:]
    s = N2.count("1")
    N2 = N2 + str(s % 2)
    s = N2.count("1")
    N2 = N2 + str(s % 2)
    R = int(N2, 2)
    if R > 85:
        print(N, R)
        break