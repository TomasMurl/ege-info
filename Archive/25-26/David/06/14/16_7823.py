from sys import setrecursionlimit
setrecursionlimit(2000)

def F(n):
    if n < 3:
        return 1
    else:
        return (n - 1) * F(n - 2)

print((F(2026) - 5 * F(2024)) / F(2022))