from sys import setrecursionlimit
setrecursionlimit(10000)

def F(n):
    if n >= 3210:
        return 1
    else:
        return F(n + 3) + 7

def G(n):
    if n < 10:
        return n
    else:
        return G(n - 3) + 5

print(F(15) - G(3000))