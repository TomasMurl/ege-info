for A in range(-100, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            F = (x * y < 2 * A) or (x >= 19) or (x < 6 * y)
            if F == False:
                flag = False
    if flag == True:
        print(A)
        break