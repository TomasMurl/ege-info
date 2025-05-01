P = range(1023, 2149)
Q = range(1362, 3899)
R = range(1813, 2567)

min_len = 1000000000000
for A_start in range(1000, 4000):
    for A_end in range(A_start + 1, 4001):
        A = range(A_start, A_end + 1)
        flag = True
        for x in range(1023, 3899):
            F = (not ((x in Q) <= ((x in P) or (x in R)))) <= ((not (x in A)) <= (not (x in Q)))
            if F == False:
                flag = False
                break
        if flag:
            min_len = min(min_len, A_end - A_start)
print(min_len)