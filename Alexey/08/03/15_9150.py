def F(x, y, A):
    return (x + y <= 27) or (y <= x - 1) or (y >= A)

for A in range(100):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)