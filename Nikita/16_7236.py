def F(n):
    if n >= 1300:
        return n
    if n < 1300 and n % 2 == 1:
        return n * F(n+1)
    if n < 1300 and n % 2 == 0:
        return n * F(n + 2) / 4

print(F(1286)/F(1290))