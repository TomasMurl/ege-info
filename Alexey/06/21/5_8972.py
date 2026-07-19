min_abs = 9999999999
for N in range(1, 1000):
    N_2 = bin(N)[2:]
    if N % 3 == 0:
        N_2 = N_2 + N_2[-3:]
    else:
        F = bin(((N % 3) * 3))[2:]
        N_2 = N_2 + F
    R = int(N_2, 2)
    if abs(130 - R) <= min_abs:
        min_abs = abs(130 - R)
        print(N, R, min_abs)

# N R   - min_abs
# 2 127 - 3
# 3 128 - 2
# 4 132 - 2