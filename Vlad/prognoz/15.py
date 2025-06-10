for A in range(0, 500):
    flag = True
    for x in range(0, 500):
        for y in range(0, 500):
            F = (x + 3 * y > A) or (x < 18) or (y < 33)
            if F == False:
                flag = False
    if flag:
        print(A)