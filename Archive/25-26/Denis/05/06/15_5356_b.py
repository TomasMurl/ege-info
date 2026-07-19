def f(x, y, A):
    return (x + y <= 22) or (y <= x - 6) or (y >= A)

for A in range(1000):
    if all( f(x, y, A) for x in range(1000) for y in range(1000)):
        print(A)