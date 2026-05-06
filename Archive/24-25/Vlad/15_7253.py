for A in range(1, 3000):
    flag = True
    for x in range(1, 3000):
        F = (x & 2735 != 0) <= ((x & 1234 == 0) <= (x & A != 0))
        if F == False:
            flag = False
    if flag:
        print(A)
        break