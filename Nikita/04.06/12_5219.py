c = 0
for n in range(1, 101):
    s = "1" + "0" * n
    while s.count("10") or s.count("1"):
        if s.count("10"):
            s = s.replace("10", "0001", 1)
        else:
            if s.count("1"):
                s = s.replace("1", "0", 1)
    if len(s) % 7 == 0:
        c += 1
print(c)