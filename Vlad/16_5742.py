from sys import setrecursionlimit
setrecursionlimit(1000000)

def F(n, m):
    if m > n:
        return 0
    if m <= n and n % m == 0:
        return 1 + F(n, m+1)
    if m <= n and n % m != 0:
        return F(n, m+1)

print(F(107864, 3))