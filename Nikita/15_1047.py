for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            F = (3 * y + 2 * x < A) or (x > 8) or (y > 12)
            if F == False:
                flag = False
    if flag == True:
        print(A)
        break
