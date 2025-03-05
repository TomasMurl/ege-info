for x in range(1, 1000):
    t = 5 ** 2026 + 7 * 5 ** 1013 + 107 - x
    n = 6
    t_6 = ""
    while t > 0:
        t_6 = str(t % n) + t_6
        t = t // n
        
    n_5 = t_6.count("5")
    n_0 = t_6.count("0")

    if n_5 - 28 == n_0:
        print(x)
        break
