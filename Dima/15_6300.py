for A in range(1, 200):
    flag = True
    for x in range(1, 200):
        F = ((x & 112 != 0) or (x & 86 != 0)) <= ((x & 65 == 0) <= (x & A != 0))
        if F == False:
            flag = False
    if flag:
        print(A)
        break