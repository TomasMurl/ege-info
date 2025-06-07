def f(x, A):
    B = range(60, 81)
    return (x % A == 0) or ((x in B) <= (not (x % 22 == 0)))

for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 1000)):
        print(A)