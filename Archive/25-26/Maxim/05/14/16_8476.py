from functools import lru_cache

@lru_cache(None)
def F(n):
    if n > 180000:
        return n ** n
    else:
        return 2 * n + F(n + 4) + F(n + 2)

for n in range(180004, 77000, -1):
    F(n)

print(F(77366))