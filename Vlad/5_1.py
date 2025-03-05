for N in range(10000, 100000):
    a_1 = str(N)[0]
    a_2 = str(N)[2]
    a_3 = str(N)[4]
    suma = int(a_1) + int(a_2) + int(a_3)
    b_1 = str(N)[1]
    b_2 = str(N)[3]
    sumb = int(b_1) + int(b_2)
    if suma > sumb:
        a_b = str(sumb) + str(suma)
    else:
        a_b = str(suma) + str(sumb)
    if a_b == "723":
        print(N)
        break
        