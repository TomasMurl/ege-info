def f(x, A):
    B = range(36, 76)
    C = range(60, 111)
    return (not (x in A)) <= ((x in B) == (x in C))

min_len = 10000000000
for l in range(0, 150):
    for r in range(l + 1, 151):
        A = range(l, r + 1)
        if all(f(x, A) for x in range(-100, 160)):
            min_len = min(min_len, r-l)
print(min_len)