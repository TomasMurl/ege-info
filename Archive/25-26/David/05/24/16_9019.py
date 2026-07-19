from sys import setrecursionlimit
setrecursionlimit(100000)

def F(n):
    if n < 12:
        return 3
    else:
        return (n + 7) * F(n - 4)

a = F(341569) // 336
b = F(341561) // 576
c = F(341557)

result = (a + b) // c
print(str(result)[-8:])