def find_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

c = 0
for i in range(900000, 0, -1):
    dels = find_dels(i)
    if len(dels) == 2:
        M = 0
    else:
        M = dels[1] + dels[-2]
    if len(str(M)) >= 3:
        if str(M)[-3:] == "112":
            print(i, M)
            c += 1
    if c == 5:
        break