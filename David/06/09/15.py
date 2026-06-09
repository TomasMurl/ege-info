def f(x, y, A):
    return (x >= 9) or (2*x < y) or (x*y < A)

for A in range(10000):
    if all(f(x, y, A) for x in range(10000) for y in range(10000)):
        print(A)
        break