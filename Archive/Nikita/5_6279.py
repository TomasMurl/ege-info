for N in range(1, 1000):
    a = bin(N)[2:]
    if N % 3 == 0:
        a = a + a[-3:]
    else:
        b = N % 3
        b = b * 3
        b = bin(b)[2:]
        a = a + b
    R = int(a, 2)
    if R > 120:
        print(N)
        break