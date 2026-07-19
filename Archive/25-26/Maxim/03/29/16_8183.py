def F(n):
    if n < 20:
        return n
    else:
        return (n - 6) * F_n[n - 7]

F_n = [None] * 50000
for i in range(len(F_n)):
    F_n[i] = F(i)

print((F_n[47872] - 290 * F_n[47865]) / F_n[47858])