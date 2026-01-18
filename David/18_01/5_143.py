for N in range(10000, 100000):
    N_str = str(N)
    sum135 = int(N_str[0]) + int(N_str[2]) + int(N_str[4]) # 43533 -> 4 + 5 + 3 = 12
    sum24 = int(N_str[1]) + int(N_str[3])
    if sum135 > sum24:
        R = str(sum24) + str(sum135)
    else:
        R = str(sum135) + str(sum24)
    if R == "723":
        print(N)
        break