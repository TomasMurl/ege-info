def find_dels(n):
    dels = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

for n in range(1324728, 2000000):
    dels = find_dels(n)
    if len(dels) == 2:
        if str(dels[0]).count('5') == 1 and str(dels[1]).count('5') == 1:
            print(n, dels[1])
    elif len(dels) == 1:
        if str(dels[0]).count('5') == 1:
            print(n, dels[0])
