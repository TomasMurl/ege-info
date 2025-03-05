maximum_nulls = 0
for x in range(1, 2031):
    n = 6 ** 2030 + 6 ** 100 - x

    n_6 = ''
    while n > 0:
        n_6 = str(n % 6) + n_6
        n = n // 6

    if n_6.count("0") > maximum_nulls:
        maximum_nulls = n_6.count("0")
print(maximum_nulls)