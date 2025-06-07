def get_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

def get_min_del(dels):
    for d in dels:
        if str(d)[-1] == "7" and d != 7 and d != n:
            return d

c = 0
for n in range(1125000, 2000000):
    dels = get_dels(n)
    min_del = get_min_del(dels)
    if min_del != None:
        c += 1
        print(n, min_del)
    if c == 5:
        break