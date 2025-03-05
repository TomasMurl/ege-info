a = []

for N in range(1, 1000):
    N2 = bin(N)[2:]
    summa = N2.count("1")
    N2 = N2 + str(summa % 2)
    summa = N2.count("1")
    N2 = N2 + str(summa % 2)
    R = int(N2, 2)
    if R > 43:
        a.append(R)

a = sorted(a)
print(a[0])