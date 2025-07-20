def F(n):
    if n < 10:
        return n
    else:
        return f[n % 10] + f[n // 10]

f = dict()

c = 0
for n in range(0, 2 ** 63):
    f[n] = F(n)
    if f[n] == 159:
        c += 1
print(c)
