def find_dels(x):
    d = {1, x} # тип данных - множество
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

c = 0
for n in range(900000, 1000000):
    ds = find_dels(n)
    if len(ds) >= 3:
        M = ds[1] + ds[-2]
    else:
        M = 0
    if str(M)[-3:] == '112':
        print(n, M)
        c += 1
        if c == 5:
            break
