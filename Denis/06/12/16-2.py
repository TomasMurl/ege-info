from sys import setrecursionlimit
setrecursionlimit(100000)

def F(n):
    if n >= 25:
        return F(n-4) + 3835
    else:
        return 8 * (G(n-7) - 31)

def G(n):
    if n >= 286702:
        return n / 20 + 27
    else:
        return G(n +11) - 5

print(F(992))