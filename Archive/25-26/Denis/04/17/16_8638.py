def F(n):
    if n <= 15:
        return 2 * n
    else:
        return n - 31 + F_n[n - 12]

F_n = [None] * 400_000
for i in range(1, 400_000):
    F_n[i] = F(i)

print((F_n[353245] - F_n[242567]) // F_n[712])