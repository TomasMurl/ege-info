from sys import setrecursionlimit
setrecursionlimit(1000000)

def F(n):
    if n <= 1:
        return n
    if n > 1 and n % 3 == 0:
        return n + F(n // 3)
    if n > 1 and n % 3 != 0:
        return n + F(n + 3)

for n in range(0, 10):
    if F(3 ** n) > 100:
        print(3 ** n, F(n))
        break