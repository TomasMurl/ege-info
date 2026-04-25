def f(x, A):
    return (x % 21 == 0) <= ((not (x % A == 0)) <= (not (x % 77 == 0)))

for A in range(1, 100000):
    if all(f(x, A) for x in range(1, 100000)):
        print(A)