a = []
for N in range(1000, 1, -1):
    N_st = N
    N_3 = ""
    while N > 0:
        N_3 = str(N % 3) + N_3
        N = N // 3
    if N_st % 3 == 0:
        N_3 = "1" + N_3 + "02"
    else:
        ost = (N_st % 3) * 4
        ost_3 = ""
        while ost > 0:
            ost_3 = str(ost % 3) + ost_3
            ost = ost // 3
        N_3 = N_3 + ost_3
    R = int(N_3, 3)
    if R < 199:
        a.append(R)
print(a)
a = sorted(a)[::-1]
print(a)
