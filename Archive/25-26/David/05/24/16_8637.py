from sys import setrecursionlimit
setrecursionlimit(10000)

def G(n):
    if n < 10:
        return 2 * n
    else:
        return G(n - 2) + 1

def F(n):
    return 2 * (G(n - 3) + 8)

print(F(15548))