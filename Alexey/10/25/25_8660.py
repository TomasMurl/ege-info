def find_dels(x):
    d = {1, x}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

c = 0
for n in range(1350050, 2000000):
    dels = find_dels(n)
    p = False
    for d in dels:
        if str(d)[-2:] == '11' and d != 11 and d != n:
            print(n, d)
            c += 1
            break
    if c == 5:
        break
# n = 398311
# dels = [1, 211, 311, 534, 398311]
# dels = [1, 256, 435, 534, 398311]