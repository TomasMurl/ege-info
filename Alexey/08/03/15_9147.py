def F(x, y, A):
    return (x > A) or (y > A) or (x + 2 * y < 80)

for A in range(100):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        print(A)