for N in range(1000, 10000):
    N_str = str(N)
    pr1 = int(N_str[0]) * int(N_str[1])
    pr2 = int(N_str[2]) * int(N_str[3])

    if pr1 > pr2:
        r = str(pr2) + str(pr1)
    else:
        r = str(pr1) + str(pr2)

    if r == "1214":
        print(N)