for A in range(1, 300):
    flag = True
    for x in range(300):
        F = (x % 33 == 0) <= ((not (x % A == 0)) <= (not (x % 242 == 0)))
        