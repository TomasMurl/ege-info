for n in range(6, 1000):
    s = "3" + "1" * n
    while "31" in s or "11111" in s or "144" in s:
        if "31" in s:
            s = s.replace("31", "4", 1)
        if "11111" in s:
            s = s.replace("11111", "33", 1)
        if "144" in s:
            s = s.replace("144", "133", 1)
    sc = sum(map(int, s))
    if sc == 160:
        print(n)
        break