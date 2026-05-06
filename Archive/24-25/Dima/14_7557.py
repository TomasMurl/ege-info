for x in range(1, 2031):
    t = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    n = 6
    t_6 = ""

    while t > 0:
        t_6 = str(t % n) + t_6
        t = t // n
    
    if t_6.count("0") == 202:
        print(x)
        break