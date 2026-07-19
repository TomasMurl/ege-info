from sys import setrecursionlimit
setrecursionlimit(10000)

def F(n):
    if n >= 10000:
        return n
    elif n < 10000 and n % 3 == 0:
        return n + F(n // 3)
    else:
        return 2 * n + F(n + 3)

print(F(999) - F(46))