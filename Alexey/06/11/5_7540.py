m = []
for N in range(1, 1000):
    N_2 = bin(N)[2:]
    sc = N_2.count('1')
    N_2 = N_2 + str(sc % 2)
    sc = N_2.count('1')
    N_2 = N_2 + str(sc % 2)
    R = int(N_2, 2)
    if R > 123:
        m.append(R)
print(min(m))