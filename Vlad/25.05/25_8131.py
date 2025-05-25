def get_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

c = 0
for x in range(500000, 1000000):
    dels = get_dels(x)
    R = str(sum(dels))
    if R[-1] == "6":
        c += 1
        print(x, R)
    if c == 5:
        break