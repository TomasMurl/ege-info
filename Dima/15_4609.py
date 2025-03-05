P = range(80, 104)
Q = range(5, 16)
R = range(35, 51)
minim = 100000
for A_start in range(1, 199):
    for A_end in range(A_start + 1, 200):
        flag = True
        A = range(A_start, A_end)
        for x in range(-100, 200):
            F = ((x in P) <= (x in Q)) or ( (not (x in A)) <= (x in R))
            if F == False:
                flag = False
        if flag:
            minim = min( len(A)-1, minim )
print(minim)