from functools import lru_cache

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    else:
        return (n - 1) * F(n - 1)

for n in range(1, 17300):
    F(n)

print((F(17258) + 3 * F(17257)) / F(17256))