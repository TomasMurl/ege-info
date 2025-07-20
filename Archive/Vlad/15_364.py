P = range(20, 51)
Q = range(10, 61)

max_A = -10000000
for A_start in range(0, 100):
    for A_end in range(A_start + 1, 101):
        A = range(A_start, A_end + 1)
        flag = True
        for x in range(1000):
            F = ((x in P) <= (x in A)) and ((x in A) <= (x in Q))
            if F == False:
                flag = False
        if flag:
            if (A_end - A_start) > max_A:
                max_A = A_end - A_start
print(max_A)