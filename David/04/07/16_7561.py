from functools import lru_cache

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n + 1) * F(n - 1)

for n in range(2025):
    F(n)

print((F(2024) - 3 * F(2023)) / F(2022))