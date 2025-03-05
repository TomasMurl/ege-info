a = []
for N in range(1, 100000):
    N2 = bin(N)[2:]
    if N % 3 == 0:
        # N2 = N2 + N2[-3] + N2[-2] + N2[-1] 
        N3 = N2 + N2[-3:0]
    else:
        ost = N % 3
        ost = ost * 3
        ost = bin(ost)[2:]
        N3 = N2 + ost
    R = int(N3, 2)
    if R >= 120:
        a.append(N)

print( min(a) )
