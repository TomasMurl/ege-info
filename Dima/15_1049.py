for A in range(0, 1000):
    P = range(253, 396)
    flag = True
    for x in range(1, 16):
        for y in range(1, 21):
            F = (y - 3 * x < A) or (x > 10) or (y > 15)
            if F == False:
                flag = False
    if flag:
        print(A)
        break