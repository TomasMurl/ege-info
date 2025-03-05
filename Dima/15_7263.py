for A in range(-1000, 1000):
    flag = False
    for x in range(0, 100):
        for y in range(0, 100):
            F = (5 * x + y > 63) or (x > 2 * y) or (3 * x + 2 * y < A)
            if F == False:
                flag = True
    if flag:
        print(A)