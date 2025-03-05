P = range(20, 31)
Q = range(5, 16)
R = range(35, 51)
min_A = 10000

for A_start in range(1, 100):
    for A_end in range(A_start + 1, 101):
        A = range(A_start, A_end)
        flag = True
        for x in range(1, 100):
            F = ((x in P) <= (x in Q)) or ((not (x in A)) <= (x in R))
            if F == False:
                flag = False
        if flag:
            min_A = min( len(A)-1, min_A )
print(min_A)