def f(x, y, A):
    return (x + 3 * y > A) or (x < 18) or (y < 33)

for A in range(0, 1000):
    if all(f(x, y, A) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)