for N in range(1, 1000):
    a = bin(N)[2:]
    if a.count("1") % 2 == 0:
        a = "10" + a[2:] + "0"
    else:
        a = "11" + a[2:] + "1"
    R = int(a, 2)
    if R > 50:
        print(N)
        break