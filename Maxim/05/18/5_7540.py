R_min = 10000000000
for N in range(1, 1000):
    N_2 = bin(N)[2:]
    N_2 = N_2 + str(N_2.count('1') % 2)
    N_2 = N_2 + str(N_2.count('1') % 2)
    R = int(N_2, 2)
    if R > 123 and R < R_min:
        R_min = R
print(R_min)