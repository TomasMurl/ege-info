for n in range(4, 10000):
    s = "1" + "9" * n
    while s.count("19") or s.count("399") or s.count("999"):
        if s.count("19"):
            s = s.replace("19", "9", 1)
        if s.count("399"):
            s = s.replace("399", "91", 1)
        if s.count("999"):
            s = s.replace("999", "3", 1)
    z = sum([int(a) for a in s])
    if z == 33:
        print(n)
        break