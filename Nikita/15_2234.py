for A in range(100, 1, -1):
    flag = True
    for x in range(1, 100):
        F = (A < 50) and ((not (x % A == 0)) <= ((x % 10 == 0) <= (not (x % 12 == 0))))
        if F == False:
            flag = False
    if flag == True:
        print(A)
        break