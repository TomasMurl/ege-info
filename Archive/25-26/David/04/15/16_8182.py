from sys import setrecursionlimit
setrecursionlimit(100000)

def F(n):
    if n >= 2025:
        return n
    else:
        return 2 * n + F(n + 2)

result = F(82) - F(81)
print(result)