def f(x, A):
    B = range(170, 221)
    return DEL(x, A) or ((x in B) <= (not DEL(x, 24)))

def DEL(n, m):
    return n % m == 0

c = 0
for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 1000)):
        c += 1
print(c)