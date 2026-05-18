min_len = 10000000
max_N = 0
for N in range(1, 1000):
    N_2 = bin(N)[2:]
    if N % 3 == 0:
        N_2 = N_2 + N_2[-3:]
    else:
        N_2 = N_2 + bin(N % 3 * 3)[2:]
    R = int(N_2, 2)
    if abs(R - 130) <= min_len:
        min_len = abs(R - 130)
        max_N = N
        print(N, R, abs(R - 130))
print(max_N)