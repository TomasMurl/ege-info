def f(x, y, A):
    return (x * y < A) or (5 * x < y) or (486 <= x)

for A in range(10000):
    if all(f(x, y, A) for x in range(10000) for y in range(10000)):
        print(A)
        break