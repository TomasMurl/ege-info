from sys import setrecursionlimit
setrecursionlimit(42100)

def F(n):
    if n == 1:
        return 1
    return (n + 1) * F(n - 1)

print((F(42038) + 3 * F(42037)) / F(42036))