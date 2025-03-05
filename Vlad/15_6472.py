P = range(135, 219)
Q = range(174, 309)
R = range(246, 383)

min_A = 10000000
for A_start in range (500):
    for A_end in range (A_start + 1, 501):
        A = range (A_start, A_end + 1)
        flag = True
        for x in range (1000):
            F = (not((x in Q) <= ((x in P) or (x in R)))) <= ((not(x in A)) <= (not(x in Q)))
            if F == False:
                flag = False
        if flag == True:
            if (A_end - A_start) < min_A:
                min_A = A_end - A_start
                print (min_A, f"{A_start}:{A_end}")