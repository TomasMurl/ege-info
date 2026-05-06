def find_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i) 
            dels.add(n // i)
    return sorted(dels)

c = 0
for i in range(2, 200001):
    dels = find_dels(i)
    if len(dels) == 2:
        c += 1
print(c)