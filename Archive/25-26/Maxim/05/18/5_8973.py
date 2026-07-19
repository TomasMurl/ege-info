R_min = 100000000000
for N in range(19, 1000):
    N_2 = bin(N)[2:] # 0b1010101
    if N % 2 == 0:
        N_2 = '10' + N_2
    else:
        N_2 = '1' + N_2 + '01'
    R = int(N_2, 2)
    if R < R_min:
        R_min = R
print(R_min)