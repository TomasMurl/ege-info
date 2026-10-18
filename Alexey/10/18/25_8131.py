def find_dels(x):
    d = {1, x} # тип данных - множество
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

c = 0
for n in range(500000, 5000000):
    dels = find_dels(n)
    R = sum(dels)
    if str(R)[-1] == '6':
        print(n, R)
        c += 1
    if c == 5:
       break
