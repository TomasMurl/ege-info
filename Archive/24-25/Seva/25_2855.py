def find_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i) 
            dels.add(n // i)
    return sorted(dels)

for i in range(326496, 649633):
    dels = find_dels(i)
    chet, nechet = 0, 0
    dels_1000 = []
    for d in dels:
        if d % 2 == 0:
            chet += 1
        else:
            nechet += 1
        if d > 1000:
            dels_1000.append(d)
    if chet == nechet and chet >= 70:
        print(i, min(dels_1000))