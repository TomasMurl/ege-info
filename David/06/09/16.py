from sys import setrecursionlimit
setrecursionlimit(100000)

def F(n):
    if n <= 7:
        return n
    else:
        return G(n - 3) * 3

def G(n):
    if n <= 7:
        return n
    else:
        return G(n - 1) + 4

print(F(43000))