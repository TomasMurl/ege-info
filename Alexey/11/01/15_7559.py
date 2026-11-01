def f(x, A):
    return (x % 33 == 0) <= ((not (x % A == 0)) <= (not (x % 242 == 0)))

for A in range(1, 10000):
    if all(f(x, A) for x in range(1, 10000)):
        print(A)
