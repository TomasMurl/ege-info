def find_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

c = 0
for i in range(1000000, 0, -1):
    dels = find_dels(i)
    if len(dels) > 2:
        M = dels[1] + dels[-2]
    else:
        M = 0
    if int(str(M)[-2:]) == 18:
        print(i, M)
        c += 1
    if c == 5:
        break