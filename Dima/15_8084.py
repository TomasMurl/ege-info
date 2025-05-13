def f(a, x, y):
    return (5 < y) or (x > 32) or (x + 2 * y < a)

for a in range(0, 500):
    if all(f(a, x, y) for x in range(0, 500) for y in range(0, 500)):
        print(a)
        break