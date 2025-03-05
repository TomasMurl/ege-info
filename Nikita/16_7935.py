from sys import setrecursionlimit
setrecursionlimit(10000000)

def F(n):
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * F(n-4)

c = (F(13766) - 9 * F(13762)) / F(13758)
print(c)