for N in range(1, 100):
    N_2 = bin(N)[2:]
    if "0" not in N_2:
        continue
    else:
        nachalo = N_2[:2]
        N_2 = N_2[::-1]
        N_2 = N_2.replace("0", nachalo[::-1], 1)
    R = int(N_2, 2)
    if R == 123:
        print(N)
        break
    
