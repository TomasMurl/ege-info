P = range(25, 38)
Q = range(32, 48)

max_len = 0

for A_start in range(0, 100):
    for A_end in range(A_start + 1, 101):
        A = range(A_start, A_end + 1)
        flag = True
        for x in range(0, 100):
            F = (( x in A ) and (not (x in P))) <= (not (x in P) and (x in Q))
            if F == False:
                flag = False
        if flag:
            max_len = max(max_len, len(A) - 1)
print(max_len)