def get_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

c = 0
for n in range(800000, 2000000):
    dels = get_dels(n)
    d_9 = 0
    for d in dels:
        if str(d)[-1] == '9' and d != 9 and d != n:
            d_9 = d
            break
    if d_9 != 0:
        print(n, d_9)
        c += 1
    if c == 5:
        break