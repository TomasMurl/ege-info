P = range(15, 41)
Q = range(21, 64)

m = []
for A_start in range(1, 100):
    for A_end in range(A_start + 1, 101):
        A = range(A_start, A_end)
        flag = True
        for x in range(1, 100):
            F = (x in P) <= (((x in Q) and (not (x in A))) <= (not (x in P)))
            if F == False:
                flag = False
        if flag:
            m.append(len(A)-1)
print(min(m))