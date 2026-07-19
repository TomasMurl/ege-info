from sys import setrecursionlimit
setrecursionlimit(1000000)
def F(n):
    if n <= 250194:
        return F(n+8) + 1050
    else:
        return 3 * (G(n-5)+27)

def G(n):
    if n >= 40:
        return G(n-3)-20
    else:
        return 30 * n + 24

print(F(10))
# 27838203