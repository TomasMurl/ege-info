from sys import setrecursionlimit
setrecursionlimit(1000000)
def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * F(n - 7)

print((F(47872) - 290 * F(47865)) / F(47858))