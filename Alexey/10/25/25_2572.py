def find_dels(x):
    d = {1, x}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

for n in range(190061, 190073):
    dels = find_dels(n)
    nd = [i for i in dels if i % 2 == 1]
    if len(nd) == 4:
        print(nd[-2], nd[-1])
