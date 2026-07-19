from sys import setrecursionlimit
setrecursionlimit(10000)

def G(n):
    if n >= 286904:
        return n / 4 + 32
    else:
        return 16 + G(n + 44)

def F(n):
    if n >= 80:
        return F(n - 8) + 3654
    else:
        return 12 * (G(n - 21) - 18)

print(F(2027))