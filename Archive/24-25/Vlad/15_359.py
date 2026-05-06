P = range(10, 26)
Q = range(15, 31)
R = range(25, 41)

max_A = -10000000
for A_start in range(1, 100):
    for A_end in range(A_start + 1, 101):
        A = range(A_start, A_end+1) # [1, 100]
        flag = False
        for x in range(1000):
            F = ((x in Q) <= (x not in R)) and (x in A) and (x not in P)
            if F == True:
                flag = True
        if flag == False:
            if (A_end - A_start) > max_A:
                max_A = A_end - A_start
print(max_A)