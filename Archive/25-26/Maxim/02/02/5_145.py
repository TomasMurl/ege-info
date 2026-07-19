for N in range(100, 1000):
    N_str = str(N)
    # N_str = "123", N = 123
    # str - для преобразования из int в str
    # int - для преобразования из str в int
    pr1 = int(N_str[0]) * int(N_str[1])
    pr2 = int(N_str[1]) * int(N_str[2])
    if pr1 > pr2:
        r = str(pr2) + str(pr1)
    else:
        r = str(pr1) + str(pr2)
    if r == "621":
        print(N)