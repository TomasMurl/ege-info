def f(x):
    p1 = x * 2
    p2 = x % 5
    return p1 + p2 - 2

a = 5
# b = a * 2 + a % 5 - 2
b = f(a)
# c = b * 2 + b % 5 - 2
c = f(b)
d = f(c)

print(a, b, c, d)