def get_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

c = 0
for n in range(1125000, 2000000):
    dels = get_dels(n)
    min_del = 0
    for d in dels:
        if str(d)[-1] == "7" and d != 7 and d != n:
            min_del = d
            break
    if min_del != 0:
        c += 1
        print(n, min_del)
    if c == 5:
        break