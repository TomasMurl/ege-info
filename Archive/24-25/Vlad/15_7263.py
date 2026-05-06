for A in range(-100, 500):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            F = (5 * x + y > 63) or (x > 2 * y) or (3 * x + 2 * y < A)
            if F == False:
                flag = False
    if not flag:
        print(A)