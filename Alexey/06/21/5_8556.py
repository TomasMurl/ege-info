for N in range(1,1000):
    N_2 = bin(N)[2:]
    if N%3 == 0:
        N_2 += N_2[-3:]
    if N%3 != 0:
        N_2 += bin((N % 3)*3)[2:]
    R = int(N_2, 2)
    if R >= 200:
        print(N)
        break