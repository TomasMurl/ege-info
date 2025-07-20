c = 0
sums = dict()
for N in range(1, 82):
    N_str = str(N)
    summa_cifr = 0
    for i in N_str:
        summa_cifr += int(i)
    if summa_cifr in sums.keys():
        if sums[summa_cifr] == 1:
            c += 1
            continue
        else:
            continue
    else:
        sums[summa_cifr] = 0
    sc_2 = bin(summa_cifr)[2:]
    if sc_2.count("1") % 2 == 0:
        sc_2 = "1" + sc_2 + "00"
    else:
        sc_2 = "10" + sc_2 + "1"
    R = int(sc_2, 2)
    if R == 21:
        sums[summa_cifr] = 1
        c += 1
    print(c, N)