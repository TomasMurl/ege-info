for A in range(0, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            F = (x+y<=30) or (y <= x + 2) or (y >= A)
            if F == False:
                flag = False
    if flag:
        print(A)