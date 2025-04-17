def find_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

c = 0
for i in range(1125000, 10 ** 100):
    dels = find_dels(i)
    good_del = 0
    for j in dels:
        if str(j)[-1] == "7" and j != 7 and j != i:
            good_del = j
            break
    if good_del != 0:
        print(i, good_del)
        c += 1
    if c == 5:
        break