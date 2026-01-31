for N in range(10000, 100000):
    N_str = str(N)
    s1 = int(N_str[0]) + int(N_str[2]) + int(N_str[4])
    s2 = int(N_str[1]) + int(N_str[3])
    if s1 > s2:
        r = str(s2) + str(s1)
    else:
        r = str(s1) + str(s2)
    if r == "723":
        print(N)
        break

    # if int(r) == 723:
    #     print(N)

