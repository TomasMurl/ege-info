P = range(5, 111)
Q = range(15, 43)
R = range(25, 71)

c = 10000
for A_start in range(1, 100):
    for A_end in range(A_start + 1, 101):
        A = range(A_start, A_end)
        flag = True
        for x in range(-100, 100):
            F = ((x in P) <= (x in Q)) or ((not(x in A)) <= (not (x in R)))
            if F == False:
                flag = False
        if flag:
            c = min( len(A)-1, c )
print(c)