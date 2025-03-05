P = range(5, 55)
Q = range(50, 94)

for A in range(-1000, 1000):
    c = 0
    for x in range(-100, 1000):
        F = ((x not in P) and (x in Q)) <= (x > A)
        if F == False:
            c += 1
    if c == 20:
        print(A, c)