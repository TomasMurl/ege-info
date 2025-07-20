for A in range(-100, 100):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            F = (5 * x + 3 * y != 60) or ((A > x) and (A > y))
            if F == False:
                flag = False
    if flag:
        print(A)
        break
