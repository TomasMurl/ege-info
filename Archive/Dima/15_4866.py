P = range(15, 34)
Q = range(45, 69)

c = 0
for A_start in range(1, 100):
    for A_end in range(A_start + 1, 101):
        A = range(A_start, A_end)
        flag = True
        for x in range(-100, 100):
            F = ((x in A) and (not (x in Q))) <= ((x in P) or (x in Q))
            if F == False:
                flag = False
        if flag:
            c = max( len(A) - 1, c )
print(c)