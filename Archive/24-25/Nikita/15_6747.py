for A in range(1, 100):
    c = 0
    n = 0
    for x in range(1, 100):
        for y in range(1, 100):
            F = (x < A) or (y < A) or ((x + 2 * y) > 50)
            n += 1
            if F == True:
                c += 1
    if c == n:
        print(A)
        break