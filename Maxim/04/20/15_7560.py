def f(x, y, A):
    return (x + y <= 30) or (y <= x + 2) or (y >= A)

for A in range(100):
    if all(f(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)