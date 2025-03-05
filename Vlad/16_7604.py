from sys import setrecursionlimit
setrecursionlimit(10000000)

def F(n):
    if n < 3:
        return 1
    if n > 2:
        return F((n+1) // 2) + 1

a = 0
for i in range(1, 2026):
    a = a + 2 ** i

print(F(a))