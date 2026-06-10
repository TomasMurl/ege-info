m = []

for N in range(19, 1000):
    N2 = bin(N)[2:]
    if N % 2 == 0:
        N2 = '10' + N2
    else:
        N2 = '1' + N2 + '01'
    R = int(N2, 2)
    m.append(R)
print(min(m))