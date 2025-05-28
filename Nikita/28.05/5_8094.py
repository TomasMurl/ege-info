for N in range(1, 1000):
    N1 = bin(N)[2:]
    if N1.count('1') % 2 == 0:
        N1 = '10' + N1[2:] + '0'
    else:
        N1 = '11' + N1[2:] + '1'
    R = int(N1, 2)
    if R > 480:
        print(N)
        break