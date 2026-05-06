maximum = 0
for x in range(1, 7 ** 400):
    n = 7 ** 400 + 7 ** 300 - x
    n_7 = ""
    while n > 0:
        n_7 = str(n % 3) + n_7
        n = n // 7
    if n_7.count("0") > maximum:
        maximum = n_7.count("0")
        print(maximum)