def f(x, A):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)

for A in range(1, 100):
    if all(f(x, A) for x in range(1, 100)):
        print(A)
        break