for A in range(1, 10000):
    flag = True
    for x in range(1, 10000):
        F = (x % 33 == 0) <= ((not (x % A == 0)) <= (not (x % 242 == 0)))
        if F == False:
            flag = False
    if flag:
        print(A)