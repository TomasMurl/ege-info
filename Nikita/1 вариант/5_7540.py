R_a = []

for N in range(1, 10000):
    N_2 = bin(N)[2:]
    summa = N_2.count('1')
    N_2 = N_2 + str(summa % 2)
    summa = N_2.count('1')
    N_2 = N_2 + str(summa % 2)
    R = int(N_2, 2)
    if R > 123:
        R_a.append(R)
print(min(R_a))