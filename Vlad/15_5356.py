for A in range(0, 100):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            F = (x + y <= 22) or (y <= x - 6) or (y >= A)
            if F == False:
                flag = False
    if flag == True:
        print(A)