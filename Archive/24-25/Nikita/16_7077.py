def G(n):
    if n < 10:
        return n
    if n >= 10:
        return G(n-2)+1

def F(n):
    return G(n-1)

c = 0
for n in range(1, 101):
    if F(n) ** (0.5) % 1 == 0 and F(n) > 0:
        c += 1
print(c)