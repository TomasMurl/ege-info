def find_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

for i in range(174457, 174506):
    dels = find_dels(i)
    if len(dels) == 4:
        print(dels[1:3])